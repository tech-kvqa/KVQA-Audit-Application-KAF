from app import app, db
from models import KAFTracking
from datetime import datetime

# Replace with your company_id
COMPANY_ID = 1  

kaf_dates = {
    "KAF1": "2026-02-05",
    "KAF2": "2026-02-07",
    "KAF3": "2026-02-07",
    "KAF4": "2026-02-07",
    "KAF5": "2026-03-05",
    "KAF6": "2026-03-05",
    "KAF7": "2026-03-05",
    "KAF8": "2026-03-16",
    "KAF9": "2026-03-16",
    "KAF10": "2026-03-16",
    "KAF12": "2026-03-08",
    "KAF13": "2026-02-28",
    "KAF14": "2026-03-16",
    "KAF15": "2026-02-08",
    "KAF17": "2026-03-18",
    "KAF18": "2026-03-16",
    "KAF19": "2026-03-16",
    "KAF20": "2026-03-16"
}

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

        # Update date
        kaf.uploaded_at = datetime.strptime(date_str, "%Y-%m-%d")

    db.session.commit()
    print("✅ KAF dates updated successfully!")