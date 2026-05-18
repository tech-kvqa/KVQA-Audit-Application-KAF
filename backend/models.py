from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Admin %r>' % self.username
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Consultant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Consultant %r>' % self.username
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

# class EMSData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     emsMethod = db.Column(db.String, nullable=True)
#     consultingAgency = db.Column(db.String, nullable=True)
#     consultant = db.Column(db.String, nullable=True)
#     consultingContractDate = db.Column(db.String, nullable=True)
#     outsourcedProcess = db.Column(db.String, nullable=True)
#     region = db.Column(db.String, nullable=True)
#     processActivity = db.Column(db.String, nullable=True)
#     processes = db.Column(db.String, nullable=True)
#     duplicatedProcess = db.Column(db.String, nullable=True)
#     numberofline = db.Column(db.String, nullable=True)
#     processname = db.Column(db.String, nullable=True)
#     Numberofemployees = db.Column(db.String, nullable=True)
#     shiftWorkers = db.Column(db.String, nullable=True)
#     shiftPersons = db.Column(db.String, nullable=True)
#     shiftsPerDay = db.Column(db.String, nullable=True)
#     internalAuditDate = db.Column(db.String, nullable=True)
#     managementReviewDate = db.Column(db.String, nullable=True)
#     certificationAuditDate = db.Column(db.String, nullable=True)
#     riskAnalysis = db.Column(db.String, nullable=True)
#     impactAnalysis = db.Column(db.String, nullable=True)
#     certificationAudit = db.Column(db.String, nullable=True)
#     nameofagency = db.Column(db.String, nullable=True)
#     time = db.Column(db.String, nullable=True)
#     environmentCertification = db.Column(db.String, nullable=True)
#     certificationstadard = db.Column(db.String, nullable=True)
#     certificationagency = db.Column(db.String, nullable=True)
#     acquisitiondate = db.Column(db.String, nullable=True)
#     environmentaccident = db.Column(db.String, nullable=True)
#     accidentdate = db.Column(db.String, nullable=True)
#     accidenttype = db.Column(db.String, nullable=True)
#     accidentNote = db.Column(db.String, nullable=True)
#     manufacturingmethod = db.Column(db.String, nullable=True)
#     locationcondition = db.Column(db.String, nullable=True)
#     environmentalload = db.Column(db.String, nullable=True)
#     wasteGas = db.Column(db.String, nullable=True)
#     wasteWater = db.Column(db.String, nullable=True)
#     wasteAmount = db.Column(db.String, nullable=True)
#     noxiousChemicals = db.Column(db.String, nullable=True)
#     pollutionBoardConsent = db.Column(db.String, nullable=True)
#     certificationNumber = db.Column(db.String, nullable=True)
#     businessType = db.Column(db.String, nullable=True)
#     numSites = db.Column(db.String, nullable=True)
#     siteLocations = db.Column(db.String, nullable=True)
#     siteField = db.Column(db.String, nullable=True)
#     siteNumber = db.Column(db.String, nullable=True)
#     siteAddress = db.Column(db.String, nullable=True)
#     signedBy = db.Column(db.String, nullable=True)
#     designation = db.Column(db.String, nullable=True)
#     director = db.Column(db.String, nullable=True)
#     finaldate = db.Column(db.String, nullable=True)

#  Not complete
class QMSData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emsMethod = db.Column(db.String, nullable=True)
    consultingAgency = db.Column(db.String, nullable=True)
    consultant = db.Column(db.String, nullable=True)
    inHouseMethodDate = db.Column(db.String, nullable=True)
    consultingContractDate = db.Column(db.String, nullable=True)
    outsourcedProcess = db.Column(db.String, nullable=True)
    region = db.Column(db.String, nullable=True)
    processActivity = db.Column(db.String, nullable=True)
    processes = db.Column(db.String, nullable=True)
    duplicatedProcess = db.Column(db.String, nullable=True)
    numberofline = db.Column(db.String, nullable=True)
    processname = db.Column(db.String, nullable=True)
    Numberofemployees = db.Column(db.String, nullable=True)
    shiftWorkers = db.Column(db.String, nullable=True)
    shiftPersons = db.Column(db.String, nullable=True)
    shiftsPerDay = db.Column(db.String, nullable=True)
    manual = db.Column(db.String, nullable=True)

class EMSData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emsMethod = db.Column(db.String(255), nullable=True)
    consultingAgency = db.Column(db.String(255), nullable=True)
    consultant = db.Column(db.String(255), nullable=True)
    consultingContractDate = db.Column(db.String, nullable=True)
    inHouseMethodDate = db.Column(db.String, nullable=True)
    outsourcedProcess = db.Column(db.String(255), nullable=True)
    region = db.Column(db.String(255), nullable=True)
    processActivity = db.Column(db.String(255), nullable=True)
    processes = db.Column(db.String, nullable=True)
    duplicatedProcess = db.Column(db.String, nullable=True)
    numberofline = db.Column(db.String(255), nullable=True)
    processname = db.Column(db.String(255), nullable=True)
    Numberofemployees = db.Column(db.String(255), nullable=True)
    shiftWorkers = db.Column(db.String(255), nullable=True)
    shiftPersons = db.Column(db.String(255), nullable=True)
    shiftsPerDay = db.Column(db.String(255), nullable=True)
    manual = db.Column(db.String(255), nullable=True)
    manualissuedate = db.Column(db.String, nullable=True)
    procedure = db.Column(db.String(255), nullable=True)
    procedureissuedate = db.Column(db.String, nullable=True)
    internalAuditDate = db.Column(db.String, nullable=True)
    managementReviewDate = db.Column(db.String, nullable=True)
    certificationAuditDate = db.Column(db.String, nullable=True)
    riskAnalysis = db.Column(db.String, nullable=True)
    impactAnalysis = db.Column(db.String, nullable=True)
    certificationAudit = db.Column(db.String, nullable=True)
    nameofagency = db.Column(db.String(255), nullable=True)
    time = db.Column(db.String, nullable=True)
    environmentCertification = db.Column(db.String, nullable=True)
    certificationstadard = db.Column(db.String(255), nullable=True)
    certificationagency = db.Column(db.String(255), nullable=True)
    acquisitiondate = db.Column(db.String, nullable=True)
    environmentaccident = db.Column(db.String, nullable=True)
    accidentNote = db.Column(db.String, nullable=True)
    accidentdate = db.Column(db.String, nullable=True)
    accidenttype = db.Column(db.String(255), nullable=True)
    manufacturingmethod = db.Column(db.String, nullable=True)
    locationcondition = db.Column(db.String, nullable=True)
    wasteGas = db.Column(db.String, nullable=True)
    wasteWater = db.Column(db.String, nullable=True)
    wasteAmount = db.Column(db.String(255), nullable=True)
    noxiousChemicals = db.Column(db.String, nullable=True)
    pollutionBoardConsent = db.Column(db.String(255), nullable=True)
    certificationNumber = db.Column(db.String(255), nullable=True)
    businessType = db.Column(db.String, nullable=True)
    numSites = db.Column(db.String(255), nullable=True)
    siteLocations = db.Column(db.String, nullable=True)

class CompanyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=True)
    address = db.Column(db.Text, nullable=True)
    department = db.Column(db.String(255), nullable=True)
    emr = db.Column(db.String(255), nullable=True)
    tel = db.Column(db.String(50), nullable=True)
    title = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    executives = db.Column(db.Integer, default=0)
    contractual = db.Column(db.Integer, default=0)
    part_time = db.Column(db.Integer, default=0)
    repetitive = db.Column(db.Integer, default=0)
    shift = db.Column(db.Integer, default=0)
    permanent = db.Column(db.Integer, default=0)
    any_other = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer, default=0)
    certification_site = db.Column(db.String(255), nullable=True)
    scope = db.Column(db.Text, nullable=True)
    standards = db.Column(db.Text, nullable=True)
    activities = db.Column(db.Text, nullable=True)
    other_activity = db.Column(db.String(255), nullable=True)
    multi_site = db.Column(db.Text, nullable=True)
    audit_desired = db.Column(db.String(255), nullable=True)
    audit_comments = db.Column(db.Text, nullable=True)
    has_multiple_sites = db.Column(db.String(10), default='no')
    manpower_details = db.Column(db.Text, nullable=True)
    additional_sites = db.Column(db.Text, nullable=True)


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Sales %r>' % self.username
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    questionnaire_type = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    token = db.Column(db.String(50), unique=True, nullable=True)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    submitted_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), default="Pending")
    decision_maker_id = db.Column(
        db.Integer,
        db.ForeignKey('decision_maker.id'),
        nullable=False,
        default=1
    )

    decision_status = db.Column(
        db.String(50),
        default="Pending",
        nullable=False
    )

class KAFDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    kaf1 = db.Column(db.String(255), nullable=True)
    kaf2 = db.Column(db.String(255), nullable=True)
    kaf3 = db.Column(db.String(255), nullable=True)
    kaf4 = db.Column(db.String(255), nullable=True)

    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class KAFTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    kaf_type = db.Column(db.String(10))  # KAF1, KAF2, KAF3, KAF4
    file_path = db.Column(db.String(255), nullable=True)
    uploaded_at = db.Column(db.DateTime, nullable=True)


class DecisionMaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)