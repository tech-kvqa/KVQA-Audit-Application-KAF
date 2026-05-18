import os
from app import app, db
from models import KAFTracking

folder = "kaf_uploads"

# Rename physical files
for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        old_path = os.path.join(folder, filename)

        new_filename = filename.replace(".pdf", ".docx")
        new_path = os.path.join(folder, new_filename)

        os.rename(old_path, new_path)

        print(f"Renamed: {filename} -> {new_filename}")

# Update database paths
with app.app_context():
    records = KAFTracking.query.all()

    for record in records:
        if record.file_path and record.file_path.endswith(".pdf"):
            record.file_path = record.file_path.replace(".pdf", ".docx")

    db.session.commit()

print("All KAF files and database paths updated successfully.")