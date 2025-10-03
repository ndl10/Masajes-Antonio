"""Simple idempotent seed script to populate the local SQLite DB with example
master services, services, therapists and per-therapist offerings.

Run while the virtualenv is active and after ensuring the app has created tables:

python backend/seed.py

"""
from app import app
from models import db, MasterServices, Services, Therapists, TherapistService

sample_master_services = [
    {'type': 'Masaje relajante'},
    {'type': 'Masaje terapéutico'},
    {'type': 'Masaje deportivo'},
]

sample_services = [
    {'name': 'Relajación 30', 'description': 'Masaje relajante 30 min', 'type_name': 'Masaje relajante', 'price': 30, 'duration': 30},
    {'name': 'Terapéutico 60', 'description': 'Masaje terapéutico 60 min', 'type_name': 'Masaje terapéutico', 'price': 50, 'duration': 60},
    {'name': 'Deportivo 45', 'description': 'Masaje deportivo 45 min', 'type_name': 'Masaje deportivo', 'price': 40, 'duration': 45},
]

sample_therapists = [
    {'name': 'Ana', 'specialty': 'Relajación'},
    {'name': 'Luis', 'specialty': 'Deportivo'},
]

sample_offerings = [
    # therapist_name, service_name, price, duration, available
    ('Ana', 'Relajación 30', 28, 30, True),
    ('Ana', 'Terapéutico 60', 55, 60, False),
    ('Luis', 'Deportivo 45', 42, 45, True),
]

with app.app_context():
    # Master services
    for m in sample_master_services:
        existing = MasterServices.query.filter_by(type=m['type']).first()
        if not existing:
            ms = MasterServices(type=m['type'])
            db.session.add(ms)
    db.session.commit()

    # Services (linking to MasterServices)
    for s in sample_services:
        master = MasterServices.query.filter_by(type=s['type_name']).first()
        if not master:
            continue
        existing = Services.query.filter_by(name=s['name']).first()
        if not existing:
            svc = Services(name=s['name'], description=s['description'], type=master.id, price=s['price'], duration=s['duration'])
            db.session.add(svc)
    db.session.commit()

    # Therapists
    for t in sample_therapists:
        existing = Therapists.query.filter_by(name=t['name']).first()
        if not existing:
            th = Therapists(name=t['name'], specialty=t['specialty'])
            db.session.add(th)
    db.session.commit()

    # Offerings
    for therapist_name, service_name, price, duration, available in sample_offerings:
        therapist = Therapists.query.filter_by(name=therapist_name).first()
        service = Services.query.filter_by(name=service_name).first()
        if not therapist or not service:
            continue
        existing = TherapistService.query.filter_by(therapist_id=therapist.id, service_id=service.id).first()
        if not existing:
            off = TherapistService(therapist_id=therapist.id, service_id=service.id, price=price, duration=duration, available=available)
            db.session.add(off)
    db.session.commit()

    print('Seeding complete')
