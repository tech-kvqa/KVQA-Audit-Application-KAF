from flask import Flask, request, jsonify, send_file
from models import *
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime, timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import os
import secrets

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'anuragiitmadras'

jwt = JWTManager(app)
db.init_app(app)

# Configure Email Sender
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "akanuragkumar75@gmail.com"
SENDER_PASSWORD = "gersqaguuxkhotwt"
SALES_EMAIL = "akanuragkumar75@gmail.com"
SALES_PASSWORD = "gersqaguuxkhotwt"

QUESTIONNAIRE_PATHS = {
    # "QMS": "questionnaire/QMS.pdf",
    # "EMS": "questionnaire/EMS.pdf",
    "ISMS": "questionnaire/ISMS.xlsx",
    # "FSMS": "questionnaire/FSMS.pdf",
    # "OHSAS": "questionnaire/OHSAS.pdf"
    "SOC2": "questionnaire/SOC2.xlsx"
}

def insert_dummy_data():
    admin_data = [
        {"email": "training@kvqaindia.com",
         "username": "Ritika", "password": "asdfgh"},
    ]

    with app.app_context():
        for data in admin_data:
            existing_admin = Admin.query.filter_by(email=data['email']).first()
            if not existing_admin:
                admin = Admin(email=data['email'], username=data['username'])
                admin.set_password(data['password'])  # ✅ Use set_password()
                db.session.add(admin)

        db.session.commit()

    consultant_data = [
        {"email": "tech@kvqaindia.com",
         "username": "Anurag", "password": "asdfgh"},
    ]

    with app.app_context():
        for data in consultant_data:
            existing_consultant = Consultant.query.filter_by(email=data['email']).first()
            if not existing_consultant:
                consultant = Consultant(email=data['email'], username=data['username'])
                consultant.set_password(data['password'])  # ✅ Use set_password()
                db.session.add(consultant)

        db.session.commit()

################################################# Home ###################################################

@app.route('/')
def hello():
    return "KVQA Reporting Application Started"

############################################### Admin Login ###############################################

@app.route('/admin/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = Admin.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify(message='Invalid username or password'), 401

############################################ Admin Protected ###############################################

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

################################################# Admin ###################################################

@app.route('/admin', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify(message='Missing required fields'), 400
    
    # Generate a token using the password
    password_token = create_access_token(identity=password)
    
    user = Admin(username=username, email=email, password=password_token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify(message='User created', token=password_token), 201

################################################# Consultant ################################################

@app.route('/consultant', methods=['POST'])
def register_consultant():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify(message='Missing required fields'), 400
    
    # Generate a token using the password
    # password_token = create_access_token(identity=password)
    hashed_password = generate_password_hash(password)
    
    user = Consultant(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify(message='User created', token=hashed_password), 201

########################################## Consultant Login ###############################################

@app.route('/consultant/login', methods=['POST'])
def consultant_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = Consultant.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify(message='Invalid username or password'), 401

############################################ Consultant Protected ###########################################


@app.route('/consultant/protected', methods=['GET'])
@jwt_required()
def consultant_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

################################################# Admin ###################################################

@app.route('/admin', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify(admins=[admin.username for admin in admins])

########################################### Consultant GET ###################################################

@app.route('/consultant', methods=['GET'])
def get_consultants():
    consultants = Consultant.query.all()
    consultant_list = [{"id": consultant.id, "email": consultant.email,
                  "username": consultant.username} for consultant in consultants]
    return jsonify({"consultants": consultant_list}), 200

############################################## Consultant Delete ############################################


@app.route('/consultant/<int:id>', methods=['DELETE'])
def delete_consultant(id):
    consultant = Consultant.query.get(id)
    if not consultant:
        return jsonify(message='Consultant not found'), 404
    db.session.delete(consultant)
    db.session.commit()
    return jsonify(message='Consultant deleted'), 200

# Function to format date into "DD-MM-YYYY"
def format_date(date_str):
    if date_str:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")  # Convert YYYY-MM-DD to DD-MM-YYYY
        except ValueError:
            return date_str  # Return as-is if invalid format
    return None

########################################## Consultant Company Data POST #####################################

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    
    new_entry = CompanyData(
        organization=data.get('organization'),
        director=data.get('director'),
        address=data.get('address'),
        department=data.get('department'),
        emr=data.get('emr'),
        tel=data.get('tel'),
        title=data.get('title'),
        email=data.get('email'),
        executives=data.get('executives', 0),
        contractual=data.get('contractual', 0),
        part_time=data.get('partTime', 0),
        repetitive=data.get('repetitive', 0),
        shift=data.get('shift', 0),
        permanent=data.get('permanent', 0),
        any_other=data.get('anyother', 0),
        total=data.get('total', 0),
        certification_site=data.get('certificationSite'),
        scope=data.get('scope'),
        standards=str(data.get('standards', {})),
        activities=str(data.get('activities', {})),
        other_activity=data.get('otherActivity'),
        multi_site=str(data.get('multiSite', {})),
        audit_desired=data.get('audit', {}).get('desired'),
        audit_comments=data.get('audit', {}).get('comments'),
        has_multiple_sites=data.get('hasMultipleSites', 'no'),
        manpower_details=str(data.get('manpowerDetails', [])),
        additional_sites=str(data.get('additionalSites', []))
    )
    
    db.session.add(new_entry)
    db.session.commit()
    
    return jsonify({"message": "Data submitted successfully"}), 201

################################################# EMS DATA GET ###################################################

@app.route('/ems_data', methods=['GET'])
def get_ems_data():
    ems_data = EMSData.query.all()
    ems_data_list = []
    for data in ems_data:
        ems_data_list.append({
            "id": data.id,
            "emsMethod": data.emsMethod,
            "consultingAgency": data.consultingAgency,
            "consultant": data.consultant,
            "consultingContractDate": data.consultingContractDate,
            "outsourcedProcess": data.outsourcedProcess,
            "region": data.region,
            "processActivity": data.processActivity,
            "processes": data.processes,
            "duplicatedProcess": data.duplicatedProcess,
            "numberofline": data.numberofline,
            "processname": data.processname,
            "Numberofemployees": data.Numberofemployees,
            "shiftWorkers": data.shiftWorkers,
            "shiftPersons": data.shiftPersons,
            "shiftsPerDay": data.shiftsPerDay,
            "internalAuditDate": data.internalAuditDate,
            "managementReviewDate": data.managementReviewDate,
            "certificationAuditDate": data.certificationAuditDate,
            "riskAnalysis": data.riskAnalysis,
            "impactAnalysis": data.impactAnalysis,
            "certificationAudit": data.certificationAudit,
            "nameofagency": data.nameofagency,
            "time": data.time,
            "environmentCertification": data.environmentCertification,
            "certificationstadard": data.certificationstadard,
            "certificationagency": data.certificationagency,
            "acquisitiondate": data.acquisitiondate,
            "environmentaccident": data.environmentaccident,
            "accidentdate": data.accidentdate,
            "accidenttype": data.accidenttype,
            "accidentNote": data.accidentNote,
            "manufacturingmethod": data.manufacturingmethod,
            "locationcondition": data.locationcondition,
            "wasteGas": data.wasteGas,
            "wasteWater": data.wasteWater,
            "wasteAmount": data.wasteAmount,
            "noxiousChemicals": data.noxiousChemicals,
            "pollutionBoardConsent": data.pollutionBoardConsent,
            "certificationNumber": data.certificationNumber,
            "businessType": data.businessType,
            "numSites": data.numSites,
            "siteLocations": data.siteLocations,
        })
    return jsonify({"ems_data": ems_data_list}), 200

################################################# EMS DATA POST ###################################################

@app.route('/ems_submit', methods=['POST'])
def submit_qms_data():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    try:
        new_entry = EMSData(
            emsMethod=str(data.get('emsMethod', '')),
            consultingAgency=data.get('consultingAgency', ''),
            consultant=data.get('consultant', ''),
            consultingContractDate=format_date(data.get('consultingContractDate', '')),
            inHouseMethodDate=format_date(data.get('inHouseMethodDate', '')),
            outsourcedProcess=str(data.get('outsourcedProcess', '')),
            region=data.get('region', ''),
            processActivity=data.get('processActivity', ''),
            processes=str(data.get('processes', '')),
            duplicatedProcess=str(data.get('duplicatedProcess', '')),
            numberofline=data.get('numberofline', ''),
            processname=data.get('processname', ''),
            Numberofemployees=data.get('Numberofemployees', ''),
            shiftWorkers=data.get('shiftWorkers', ''),
            shiftPersons=data.get('shiftPersons', ''),
            shiftsPerDay=data.get('shiftsPerDay', ''),
            manual=data.get('manual', ''),
            manualissuedate=format_date(data.get('manualissuedate', '')),
            procedure=data.get('procedure', ''),
            procedureissuedate=format_date(data.get('procedureissuedate', '')),
            internalAuditDate=format_date(data.get('internalAuditDate', '')),
            managementReviewDate=format_date(data.get('managementReviewDate', '')),
            certificationAuditDate=format_date(data.get('certificationAuditDate', '')),
            riskAnalysis=str(data.get('riskAnalysis', '')),
            impactAnalysis=str(data.get('impactAnalysis', '')),
            certificationAudit=str(data.get('certificationAudit', '')),
            nameofagency=data.get('nameofagency', ''),
            time=format_date(data.get('time', '')),
            environmentCertification=str(data.get('environmentCertification', '')),
            certificationstadard=data.get('certificationstadard', ''),
            certificationagency=data.get('certificationagency', ''),
            acquisitiondate=format_date(data.get('acquisitiondate', '')),
            environmentaccident=str(data.get('environmentaccident', '')),
            accidentNote=data.get('accidentNote', ''),
            accidentdate=format_date(data.get('accidentdate', '')),
            accidenttype=data.get('accidenttype', ''),
            manufacturingmethod=str(data.get('manufacturingmethod', '')),
            locationcondition=str(data.get('locationcondition', '')),
            wasteGas=str(data.get('wasteGas', '')),
            wasteWater=str(data.get('wasteWater', '')),
            wasteAmount=data.get('wasteAmount', ''),
            noxiousChemicals=str(data.get('noxiousChemicals', '')),
            pollutionBoardConsent=data.get('pollutionBoardConsent', ''),
            certificationNumber=data.get('certificationNumber', ''),
            businessType=str(data.get('businessType', '')),
            numSites=data.get('numSites', ''),
            siteLocations=data.get('siteLocations', '')
        )

        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"message": "Data submitted successfully"}), 201  # Success response

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500  # Return error message
    
################################################# QMS Data Get ###################################################
    
@app.route('/qms_data', methods=['GET'])
def get_qms_data():
    qms_data = QMSData.query.all()
    qms_data_list = []
    for data in qms_data:
        qms_data_list.append({
            "id": data.id,
            "emsMethod": data.emsMethod,
            "consultingAgency": data.consultingAgency,
            "consultant": data.consultant,
            "consultingContractDate": data.consultingContractDate,
            "inHouseMethodDate": data.inHouseMethodDate,
            "outsourcedProcess": data.outsourcedProcess,
            "region": data.region,
            "processActivity": data.processActivity,
            "processes": data.processes,
            "duplicatedProcess": data.duplicatedProcess,
            "numberofline": data.numberofline,
            "processname": data.processname,
            "Numberofemployees": data.Numberofemployees,
            "shiftWorkers": data.shiftWorkers,
            "shiftPersons": data.shiftPersons,
            "shiftsPerDay": data.shiftsPerDay,

        })
    return jsonify({"qms_data": qms_data_list}), 200

################################################# Company Data GET ###################################################

@app.route('/company_data', methods=['GET'])
def get_company_data():
    comp_data = CompanyData.query.all()
    comp_data_list = []
    for data in comp_data:
        comp_data_list.append({
            "id": data.id,
            "organization": data.organization,
            "director":data.director,
            "address":data.address,
            "department":data.department,
            "emr":data.emr,
            "tel":data.tel,
            "title":data.title,
            "email":data.email,
            "executives":data.executives,
            "contractual":data.contractual,
            "part_time":data.part_time,
            "repetitive":data.repetitive,
            "shift":data.shift,
            "permanent":data.permanent,
            "any_other":data.any_other,
            "total":data.total,
            "certification_site":data.certification_site,
            "scope":data.scope,
            "standards":data.standards,
            "activities":data.activities,
            "other_activity":data.other_activity,
            "multi_site":data.multi_site,
            "audit_desired":data.audit_desired,
            "audit_comments":data.audit_comments,
            "has_multiple_sites":data.has_multiple_sites,
            "manpower_details":data.manpower_details,
            "additional_sites":data.additional_sites
        })
    return jsonify({"comp_data": comp_data_list}), 200

################################################# Sales Login ###############################################

@app.route('/sales/login', methods=['POST'])
def sales_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = Sales.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify(message='Invalid username or password'), 401

@app.route('/sales', methods=['POST'])
def register_sales():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify(message='Missing required fields'), 400
    
    # Generate a token using the password
    # password_token = create_access_token(identity=password)
    hashed_password = generate_password_hash(password)
    
    user = Sales(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify(message='User created', token=hashed_password), 201


@app.route('/sales', methods=['GET'])
def get_sales():
    sales = Sales.query.all()
    sales_list = [{"id": sale.id, "email": sale.email,
                  "username": sale.username} for sale in sales]
    return jsonify({"Sales": sales_list}), 200


@app.route('/sales/<int:id>', methods=['DELETE'])
def delete_sales(id):
    sales = Sales.query.get(id)
    if not sales:
        return jsonify(message='Sales not found'), 404
    db.session.delete(sales)
    db.session.commit()
    return jsonify(message='Sales Executive deleted'), 200

@app.route('/sales/get-questionnaire-types', methods=['GET'])
def get_questionnaire_types():
    return jsonify(list(QUESTIONNAIRE_PATHS.keys()))

# @app.route('/sales/send-email', methods=['POST'])
# def send_email():
#     data = request.json
#     company_name = data.get('company_name')
#     address = data.get('address')
#     director = data.get('director')
#     email = data.get('email')
#     questionnaire_type = data.get('questionnaire_type')

#     # Get the questionnaire file path
#     file_path = QUESTIONNAIRE_PATHS.get(questionnaire_type)
#     if not file_path or not os.path.exists(file_path):
#         return jsonify({'error': 'Questionnaire file not found'}), 404

#     # Save company record
#     company = Company(name=company_name, address=address, director=director, email=email,
#                       questionnaire_type=questionnaire_type, file_path=file_path)
#     db.session.add(company)
#     db.session.commit()

#     # Create Email Message
#     msg = EmailMessage()
#     msg["Subject"] = f"Certification Questionnaire - {questionnaire_type}"
#     msg["From"] = SENDER_EMAIL
#     msg["To"] = email
#     msg.set_content(f"Dear {director},\n\nPlease find attached the {questionnaire_type} questionnaire.")

#     # Attach the Questionnaire File
#     with open(file_path, "rb") as attachment:
#         msg.add_attachment(attachment.read(), maintype="application", subtype="pdf", filename=os.path.basename(file_path))

#     # Send Email
#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()  # Secure connection
#             server.login(SENDER_EMAIL, SENDER_PASSWORD)
#             server.send_message(msg)

#         return jsonify({'message': 'Email sent successfully'})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@app.route('/sales/send-email', methods=['POST'])
def send_email():
    data = request.json
    company_name = data.get('company_name')
    address = data.get('address')
    director = data.get('director')
    email = data.get('email')
    questionnaire_type = data.get('questionnaire_type')

    # Get the questionnaire file path
    file_path = QUESTIONNAIRE_PATHS.get(questionnaire_type)
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': 'Questionnaire file not found'}), 404

    # Generate a unique token for the company
    token = secrets.token_urlsafe(16)  # Generates a secure token

    # Save company record in the database
    company = Company(name=company_name, address=address, director=director, email=email,
                      questionnaire_type=questionnaire_type, file_path=file_path, token=token, status="Pending")
    db.session.add(company)
    db.session.commit()

    # Create Email Message
    submission_link = f"http://127.0.0.1:8080/upload/{token}"
    msg = EmailMessage()
    msg["Subject"] = f"Certification Questionnaire - {questionnaire_type}"
    msg["From"] = SENDER_EMAIL
    msg["To"] = email
    msg.set_content(f"""
    Dear {director},

    Please find attached the {questionnaire_type} questionnaire. 

    After filling out the questionnaire, please submit it using the link below:

    {submission_link}

    Regards,
    Your Team
    """)

    # Attach the Questionnaire File
    with open(file_path, "rb") as attachment:
        msg.add_attachment(attachment.read(), maintype="application", subtype="pdf", filename=os.path.basename(file_path))

    # Send Email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        return jsonify({'message': 'Email sent successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sales/get-companies', methods= ['GET'])
def get_companies():
    company = Company.query.all()
    company_list = [{
        "id": c.id,
        "name": c.name,
        "email": c.email,
        "director": c.director,
        "audit_type": c.questionnaire_type,
        "date_sent": c.sent_at.strftime("%d-%m-%Y"),
        "status": c.status,
        "token": c.token,
        "address": c.address,
        "submitted_at": c.submitted_at.strftime("%d-%m-%Y") if c.submitted_at else "Not Submitted"
    } for c in company]

    return jsonify(company_list)


@app.route('/sales/delete-company/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    company = Company.query.get(company_id)
    if not company:
        return jsonify({"error": "Company not found"}), 404

    try:
        db.session.delete(company)
        db.session.commit()
        return jsonify({"message": "Company deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@app.route('/sales/upload', methods=['POST'])
def upload_file():
    token = request.form.get('token')
    file = request.files.get('file')

    company = Company.query.filter_by(token=token).first()
    if not company:
        return jsonify({"error": "Invalid link"}), 404

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Save the file to a designated folder
    upload_folder = "uploaded_forms"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, f"{company.name}_{company.questionnaire_type}.xlsx")
    file.save(file_path)

    # Update company record
    company.status = "Submitted"
    # company.submitted_at = datetime.utcnow()
    company.submitted_at = datetime.now(timezone.utc)
    db.session.commit()

    notify_sales_executive(company, file_path)

    return jsonify({"message": "File uploaded successfully"}), 200


def notify_sales_executive(company, file_path):
    sales_email = "tech@kvqaindia.com"
    subject = f"Form Submission Received - {company.name}"
    body = f"""
    Dear Sales Team,

    {company.name} has submitted their filled questionnaire for {company.questionnaire_type}.
    You can now proceed with sending the quotation.

    Best Regards,
    KVQA Audit System
    """

    send_email(sales_email, subject, body, file_path)


def send_email(to_email, subject, body, file_path):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SALES_EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with open(file_path, "rb") as attachment:
            msg.add_attachment(
                attachment.read(),
                maintype="application",
                subtype="octet-stream",  # Generic binary stream
                filename=os.path.basename(file_path),
            )

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SALES_EMAIL, SALES_PASSWORD)
            server.send_message(msg)

    except Exception as e:
        print("Error sending notification:", e)

@app.route('/sales/get-uploaded-form/<company_name>/<questionnaire_type>', methods=['GET'])
def get_uploaded_form(company_name, questionnaire_type):
    upload_folder = "uploaded_forms"
    file_path = os.path.join(upload_folder, f"{company_name}_{questionnaire_type}.xlsx")

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(file_path, as_attachment=False, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/upload-kaf/<token>', methods=['POST'])
def upload_kaf_files(token):
    company = Company.query.filter_by(token=token).first()

    if not company:
        return jsonify({"error": "Invalid token"}), 404

    upload_folder = "kaf_uploads"
    os.makedirs(upload_folder, exist_ok=True)

    kaf_doc = KAFDocument.query.filter_by(company_id=company.id).first()

    if not kaf_doc:
        kaf_doc = KAFDocument(company_id=company.id)

    # for kaf in ["KAF1", "KAF2", "KAF3", "KAF4"]:
    ALL_KAFS = [
        "KAF1","KAF2","KAF3","KAF4","KAF5","KAF6","KAF7","KAF8",
        "KAF9","KAF10","KAF12","KAF13","KAF14","KAF15",
        "KAF17","KAF18","KAF19","KAF20","KAF24"
    ]

    for kaf in ALL_KAFS:
        file = request.files.get(kaf)

        if file:
            filename = f"{company.name}_{kaf}.pdf"
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)

            setattr(kaf_doc, kaf.lower(), filepath)

    db.session.add(kaf_doc)
    db.session.commit()

    return jsonify({"message": "KAF files uploaded successfully"})

@app.route('/get-kaf/<int:company_id>/<kaf_type>', methods=['GET'])
def get_kaf_file(company_id, kaf_type):
    kaf_doc = KAFDocument.query.filter_by(company_id=company_id).first()

    if not kaf_doc:
        return jsonify({"file_url": None})

    file_path = getattr(kaf_doc, kaf_type.lower(), None)

    if not file_path or not os.path.exists(file_path):
        return jsonify({"file_url": None})

    return jsonify({
        "file_url": f"http://127.0.0.1:5000/{file_path}"
    })

@app.route('/kaf_uploads/<filename>')
def serve_kaf_file(filename):
    return send_file(os.path.join("kaf_uploads", filename))

@app.route('/kaf-status/<int:company_id>', methods=['GET'])
def get_kaf_status(company_id):
    kafs = KAFTracking.query.filter_by(company_id=company_id).all()

    kaf_map = {k.kaf_type: k for k in kafs}

    result = []
    # for kaf in ["KAF1", "KAF2", "KAF3", "KAF4"]:
    ALL_KAFS = [
        "KAF1","KAF2","KAF3","KAF4","KAF5","KAF6","KAF7","KAF8",
        "KAF9","KAF10","KAF12","KAF13","KAF14","KAF15",
        "KAF17","KAF18","KAF19","KAF20","KAF24"
    ]

    for kaf in ALL_KAFS:
        record = kaf_map.get(kaf)

        result.append({
            "kaf_type": kaf,
            "date": record.uploaded_at.strftime("%d-%m-%Y") if record and record.uploaded_at else "",
            "file_exists": True if record and record.file_path else False
        })

    return jsonify(result)

@app.route('/upload-kaf/<int:company_id>/<kaf_type>', methods=['POST'])
def upload_kaf(company_id, kaf_type):
    file = request.files.get('file')

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    upload_folder = "kaf_uploads"
    os.makedirs(upload_folder, exist_ok=True)

    filename = f"{company_id}_{kaf_type}.docx"
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)

    kaf = KAFTracking.query.filter_by(company_id=company_id, kaf_type=kaf_type).first()

    if not kaf:
        kaf = KAFTracking(company_id=company_id, kaf_type=kaf_type)

    kaf.file_path = filepath
    kaf.uploaded_at = datetime.utcnow()

    db.session.add(kaf)
    db.session.commit()

    return jsonify({"message": "Uploaded successfully"})

@app.route('/view-kaf/<int:company_id>/<kaf_type>', methods=['GET'])
def view_kaf(company_id, kaf_type):
    kaf = KAFTracking.query.filter_by(company_id=company_id, kaf_type=kaf_type).first()

    if not kaf or not kaf.file_path:
        return jsonify({"error": "File not found"}), 404

    # ✅ Get company name
    company = Company.query.get(company_id)
    company_name = company.name.replace(" ", "_") if company else "Company"

    # ✅ Extract extension dynamically
    ext = os.path.splitext(kaf.file_path)[1]  # .docx / .pdf

    # ✅ Final filename
    filename = f"{company_name}_{kaf_type}{ext}"

    return send_file(
        kaf.file_path,
        as_attachment=True,
        download_name=filename
    )

@app.route('/company/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    if not company:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": company.id,
        "name": company.name
    })


###################################### Decision Maker Login ######################################

@app.route('/decision-maker', methods=['POST'])
def register_decision_maker():
    data = request.get_json()

    user = DecisionMaker(
        username=data['username'],
        email=data['email']
    )
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Decision Maker created"}), 201

@app.route('/decision-maker/login', methods=['POST'])
def decision_maker_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = DecisionMaker.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={
            "id": user.id,
            "username": user.username,
            "role": "decision_maker"
        })

        return jsonify(
            access_token=access_token,
            decision_maker_id=user.id,
            username=user.username
        ), 200

    return jsonify(message='Invalid username or password'), 401

@app.route('/assign-decision-maker/<int:company_id>', methods=['POST'])
def assign_decision_maker(company_id):
    data = request.get_json()

    company = Company.query.get(company_id)

    if not company:
        return jsonify({"error": "Company not found"}), 404

    company.decision_maker_id = data['decision_maker_id']

    db.session.commit()

    return jsonify({"message": "Decision maker assigned successfully"})

# @app.route('/decision-maker/applications/<int:decision_maker_id>', methods=['GET'])
# def get_decision_maker_applications(decision_maker_id):

#     companies = Company.query.filter_by(
#         decision_maker_id=decision_maker_id
#     ).all()

#     result = []

#     for company in companies:
#         kafs = KAFTracking.query.filter_by(company_id=company.id).all()

#         if any(k.file_path for k in kafs):
#             result.append({
#                 "company_id": company.id,
#                 "company_name": company.name,
#                 "decision_status": company.decision_status,
#                 "submitted_at": company.submitted_at.strftime("%d-%m-%Y") if company.submitted_at else ""
#             })

#     return jsonify(result)

@app.route('/decision-maker/applications/<int:decision_maker_id>', methods=['GET'])
def get_decision_maker_applications(decision_maker_id):

    companies = Company.query.filter_by(
        decision_maker_id=decision_maker_id
    ).all()

    result = []

    for company in companies:
        kafs = KAFTracking.query.filter_by(company_id=company.id).all()

        # Only show companies where at least one KAF file exists
        if any(k.file_path for k in kafs):

            # Prefer submitted_at, fallback to sent_at
            if company.submitted_at:
                submitted_date = company.submitted_at.strftime("%d-%m-%Y")
            elif company.sent_at:
                submitted_date = company.sent_at.strftime("%d-%m-%Y")
            else:
                submitted_date = ""

            result.append({
                "company_id": company.id,
                "company_name": company.name,
                "decision_status": company.decision_status,
                "submitted_at": submitted_date
            })

    return jsonify(result)

@app.route('/decision-maker/decision/<int:company_id>', methods=['POST'])
def make_decision(company_id):
    data = request.get_json()

    company = Company.query.get(company_id)

    if not company:
        return jsonify({"error": "Company not found"}), 404

    decision = data.get("decision")

    if decision not in ["Approved", "Rejected"]:
        return jsonify({"error": "Invalid decision"}), 400

    company.decision_status = decision

    db.session.commit()

    return jsonify({
        "message": f"Project {decision.lower()} successfully"
    })


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_dummy_data()
        app.run(debug=True)