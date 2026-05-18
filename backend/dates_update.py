# from app import app, db
# from models import KAFTracking
# from datetime import datetime

# # Replace with your company_id
# COMPANY_ID = 9 

# kaf_dates = {
#     "KAF1": "11-08-2025",
#     "KAF2": "24-09-2025",
#     "KAF3": "24-09-2025",
#     "KAF4": "24-09-2025",
#     "KAF5": "22-OCT-2025",
#     "KAF6": "22-OCT-2025",
#     "KAF7": "22-OCT-2025",
#     "KAF8": "06-NOV 2025",
#     "KAF9": "06-NOV 2025",
#     "KAF10": "06-NOV 2025",
#     "KAF12": "22-OCT-2025",
#     "KAF13": "22-OCT-2025",
#     "KAF14": "06-NOV 2025",
#     "KAF15": "24-09-2025",
#     "KAF17": "06-NOV 2025",
#     "KAF18": "06-NOV 2025",
#     "KAF19": "06-NOV 2025",
#     "KAF20": "06-NOV 2025"
# }

# with app.app_context():
#     for kaf_type, date_str in kaf_dates.items():

#         kaf = KAFTracking.query.filter_by(
#             company_id=COMPANY_ID,
#             kaf_type=kaf_type
#         ).first()

#         # Create record if missing
#         if not kaf:
#             kaf = KAFTracking(
#                 company_id=COMPANY_ID,
#                 kaf_type=kaf_type
#             )
#             db.session.add(kaf)

#         # Update date
#         kaf.uploaded_at = datetime.strptime(date_str, "%Y-%m-%d")

#     db.session.commit()
#     print("✅ KAF dates updated successfully!")


# from app import app, db
# from models import KAFTracking
# from datetime import datetime

# # Replace with your company_id
# COMPANY_ID = 3

# kaf_dates = {
#     "KAF1": "31-12-2025",
#     "KAF2": "06-02-2026",
#     "KAF3": "06-02-2026",
#     "KAF4": "06-02-2026",
#     "KAF5": "07-03-2026",
#     "KAF6": "07-03-2026",
#     "KAF7": "07-03-2026",
#     "KAF8": "20-March-2026",
#     "KAF9": "20-March-2026",
#     "KAF10": "20-March-2026",
#     "KAF12": "10-03-2026",
#     "KAF13": "28-02-2026",
#     "KAF14": "20-March-2026",
#     "KAF15": "06-02-2026",
#     "KAF17": "20-March-2026",
#     "KAF18": "20-March-2026",
#     "KAF19": "20-March-2026",
#     "KAF20": "20-March-2026",
#     "KAF24": "02-04-2026"
# }

# def parse_date(date_str):
#     """
#     Supports:
#     - 11-08-2025
#     - 24-09-2025
#     - 22-OCT-2025
#     - 06-NOV-2025
#     """
#     try:
#         # Numeric month format
#         return datetime.strptime(date_str, "%d-%m-%Y")
#     except ValueError:
#         # Text month format
#         return datetime.strptime(date_str, "%d-%b-%Y")


# with app.app_context():
#     for kaf_type, date_str in kaf_dates.items():

#         kaf = KAFTracking.query.filter_by(
#             company_id=COMPANY_ID,
#             kaf_type=kaf_type
#         ).first()

#         # Create record if missing
#         if not kaf:
#             kaf = KAFTracking(
#                 company_id=COMPANY_ID,
#                 kaf_type=kaf_type
#             )
#             db.session.add(kaf)

#         # Normalize month capitalization
#         normalized_date = date_str.upper().replace(" ", "-")

#         # Convert date
#         kaf.uploaded_at = parse_date(normalized_date.title())

#     db.session.commit()

#     print(f"✅ KAF dates updated successfully for company {COMPANY_ID}!")


from app import app, db
from models import KAFTracking
from datetime import datetime

# Replace with your company_id
COMPANY_ID = 7

kaf_dates = {
    "KAF1": "13-12-2025",
    "KAF2": "11-02-2026",
    "KAF3": "11-02-2026",
    "KAF4": "11-02-2026",
    "KAF5": "07-03-2026",
    "KAF6": "07-03-2026",
    "KAF7": "07-03-2026",
    "KAF8": "22-03-2026",
    "KAF9": "22-03-2026",
    "KAF10": "22-03-2026",
    "KAF12": "09-03-2026",
    "KAF13": "28-02-2026",
    "KAF14": "22-03-2026",
    "KAF15": "07-03-2026",
    "KAF17": "22-03-2026",
    "KAF18": "22-03-2026",
    "KAF19": "22-03-2026",
    "KAF20": "22-03-2026",
    "KAF24": "24-03-2026"
}

def parse_date(date_str):
    """
    Supports:
    - 31-12-2025
    - 22-OCT-2025
    - 20-March-2026
    - 20-NOVEMBER-2026
    """
    formats = [
        "%d-%m-%Y",   # Numeric month
        "%d-%b-%Y",   # Short month name (Oct)
        "%d-%B-%Y"    # Full month name (March)
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Unsupported date format: {date_str}")


with app.app_context():
    for kaf_type, date_str in kaf_dates.items():

        kaf = KAFTracking.query.filter_by(
            company_id=COMPANY_ID,
            kaf_type=kaf_type
        ).first()

        # Create record if missing
        if not kaf:
            kaf = KAFTracking(
                company_id=COMPANY_ID,
                kaf_type=kaf_type
            )
            db.session.add(kaf)

        # Clean formatting
        normalized_date = date_str.strip().replace(" ", "-")

        # Convert date
        kaf.uploaded_at = parse_date(normalized_date)

        print(f"Updated {kaf_type}: {normalized_date}")

    db.session.commit()

    print(f"\n✅ KAF dates updated successfully for company {COMPANY_ID}!")