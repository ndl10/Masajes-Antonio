from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# USUARIOS
# -------------------
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='cliente')
    image = db.Column(db.String(75), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "image": self.image
        }


class Therapist(db.Model):
    __tablename__ = "therapists"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=True)

    offerings = db.relationship("Offering", back_populates="therapist", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialty": self.specialty,
            "image": self.image,
        }


class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=True)

    offerings = db.relationship("Offering", back_populates="service", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "duration": self.duration,
            "image": self.image,
        }


class Offering(db.Model):
    """Tabla intermedia: qué servicios da cada masajista y en qué condiciones"""
    __tablename__ = "offerings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    therapist_id = db.Column(db.Integer, db.ForeignKey("therapists.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)

    therapist = db.relationship("Therapist", back_populates="offerings")
    service = db.relationship("Service", back_populates="offerings")

    def serialize(self):
        return {
            "id": self.id,
            "therapist_id": self.therapist_id,
            "therapist_name": self.therapist.name if self.therapist else None,
            "service_id": self.service_id,
            "service_name": self.service.name if self.service else None,
            "price": self.price,
            "duration": self.duration,
            "available": self.available,
        }
