from app import app, db
from models import DecisionMaker

def insert_decision_maker():
    with app.app_context():

        # Check if already exists
        existing_user = DecisionMaker.query.filter_by(email="tech@kvqaindia.com").first()

        if existing_user:
            print("Decision Maker already exists.")
            return

        # Create decision maker
        decision_maker = DecisionMaker(
            id=1,
            username="Anurag",
            email="tech@kvqaindia.com"
        )

        decision_maker.set_password("asdfgh")

        db.session.add(decision_maker)
        db.session.commit()

        print("Decision Maker inserted successfully.")

if __name__ == "__main__":
    insert_decision_maker()