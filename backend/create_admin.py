from app import app
from models import db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Verifica si ya existe un admin
    existing = User.query.filter_by(email="admin@toninmasajes.com").first()
    if existing:
        print("El admin ya existe en la base de datos.")
    else:
        admin = User(
            name="Creador",
            email="admin@toninmasajes.com",
            password=generate_password_hash("admin123"),
            role="admin",
            image=None
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin creado con éxito!")

