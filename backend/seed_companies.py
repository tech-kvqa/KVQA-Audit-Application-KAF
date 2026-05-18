# from app import app, db
# from models import Company
# from datetime import datetime
# import secrets

# # companies_data = [
# #     ("Cynet Health Inc.", "28 March 2025"),
# #     ("Cynet Health India Pvt Ltd", "28 March 2025"),
# #     ("Cynet Locums Inc", "28 March 2025"),
# #     ("Cynet Systems Inc.", "28 March 2025"),
# #     ("Cynet Systems Pvt Ltd", "28 March 2025"),
# #     ("Mobideo Technologies Ltd.", "16 June 2025"),
# #     ("Mobideo Technologies (US) Inc.", "16 June 2025"),
# #     ("M.I.V.B INFORMATION TECHNOLOGY", "08 July 2025"),
# #     ("MIVB Information Technology Inc.", "08 July 2025"),
# #     ("Swarmnetics Pte. Ltd.", "01 November 2025"),
# #     ("Swarmnetics (B) Sdn Bhd", "01 November 2025"),
# # ]

# companies_data = [
#     ("Cargomar PVT Ltd", "31-12-2025", "QMS"),
#     #EMS
#     ("BHAV EXIM PVT LTD", "09-06-2025", "EMS"),
#     ("DEWAN SONS EXPORTS PRIVATE LIMITED" "14-08-2025", "EMS"),
#     ("UTSAH ENGINEERING PRIVATE LIMITED", "03-01-2026", "EMS")
#     #OHS
#     ("Guardians Casting Pvt Ltd", "13-12-2025", "OHS"),
#     ("DIE MOULD SOLUTIONS","24-12-2024", "OHS")
#     #QMS
#     ("Neelu Packaging Industries", "11-08-2025", "QMS"),
#     ("CREEMOS INTERNATIONAL LIMITED", "21-06-2025", "QMS"),
#     ("SRI KALYAN EXPORT PVT_ LTD_", "05-04-2025", "QMS"),
#     ("NANDI AGRICULTURAL INDUSTRIES", "01-01-2026", "QMS")
# ]

# def parse_date(date_str):
#     return datetime.strptime(date_str, "%d %B %Y")

# with app.app_context():
#     for name, issue_date in companies_data:

#         existing = Company.query.filter_by(name=name).first()
#         if existing:
#             continue

#         company = Company(
#             name=name,
#             address="N/A",
#             director="N/A",
#             email="custom@email.com",
#             questionnaire_type="ISMS",
#             file_path="dummy/path/file.docx",   # ✅ FIX HERE
#             token=secrets.token_urlsafe(16),
#             sent_at=parse_date(issue_date),
#             status="Pending"
#         )

#         db.session.add(company)

#     db.session.commit()

# print("✅ Companies inserted successfully")


from app import app, db
from models import Company
from datetime import datetime
import secrets

companies_data = [
    # QMS
    ("Cargomar PVT Ltd", "31-12-2025", "QMS"),

    # EMS
    ("BHAV EXIM PVT LTD", "09-06-2025", "EMS"),
    ("DEWAN SONS EXPORTS PRIVATE LIMITED", "14-08-2025", "EMS"),
    ("UTSAH ENGINEERING PRIVATE LIMITED", "03-01-2026", "EMS"),

    # OHS
    ("Guardians Casting Pvt Ltd", "13-12-2025", "OHS"),
    ("DIE MOULD SOLUTIONS", "24-12-2024", "OHS"),

    # QMS
    ("Neelu Packaging Industries", "11-08-2025", "QMS"),
    ("CREEMOS INTERNATIONAL LIMITED", "21-06-2025", "QMS"),
    ("SRI KALYAN EXPORT PVT LTD", "05-04-2025", "QMS"),
    ("NANDI AGRICULTURAL INDUSTRIES", "01-01-2026", "QMS")
]

def parse_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y")

with app.app_context():

    for name, issue_date, questionnaire_type in companies_data:

        existing = Company.query.filter_by(name=name).first()
        if existing:
            print(f"Skipping existing company: {name}")
            continue

        company = Company(
            name=name,
            address="N/A",
            director="N/A",
            email="custom@email.com",

            # ✅ Dynamic questionnaire type from tuple
            questionnaire_type=questionnaire_type,

            file_path="dummy/path/file.docx",
            token=secrets.token_urlsafe(16),

            sent_at=parse_date(issue_date),

            status="Pending",
            decision_maker_id=1,
            decision_status="Pending"
        )

        db.session.add(company)

    db.session.commit()

print("✅ Companies inserted successfully")