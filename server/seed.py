#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app
from models import db, Employee, Review, Onboarding

with app.app_context():
    # Delete all rows in tables
    db.session.query(Review).delete()
    db.session.query(Onboarding).delete()
    db.session.query(Employee).delete()

    # Add employees
    uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
    tristan = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))
    db.session.add_all([uri, tristan])
    db.session.commit()  # Commit so they get IDs

    # Add reviews (1..many with Employee)
    uri_2023 = Review(employee_id=uri.id, year=2023, summary="Great web developer!")
    tristan_2021 = Review(employee_id=tristan.id, year=2021, summary="Good coding skills, often late to work")
    tristan_2022 = Review(employee_id=tristan.id, year=2022, summary="Strong coding skills, takes long lunches")
    tristan_2023 = Review(employee_id=tristan.id, year=2023, summary="Awesome coding skills, dedicated worker")
    
    db.session.add_all([uri_2023, tristan_2021, tristan_2022, tristan_2023])
    db.session.commit()

    # Add onboarding (1..1 with Employee)
    uri_onboarding = Onboarding(employee_id=uri.id, orientation=datetime.datetime(2023, 3, 27))
    tristan_onboarding = Onboarding(employee_id=tristan.id, orientation=datetime.datetime(2020, 1, 20, 14, 30), forms_complete=True)

    db.session.add_all([uri_onboarding, tristan_onboarding])
    db.session.commit()

    print("Database seeded successfully!")
