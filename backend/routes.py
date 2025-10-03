from flask import Blueprint, request, jsonify
from models import db, User, Therapist, Service, Offering
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from functools import wraps

main = Blueprint('main', __name__)

# ------------------------
# DECORADOR ADMIN
# ------------------------
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        identity = get_jwt_identity()  # {"id":..., "role":...}
        if identity.get("role") != "admin":
            return jsonify({"error": "Acceso denegado: solo administradores"}), 403
        return fn(*args, **kwargs)
    return wrapper

# ------------------------
# LOGIN
# ------------------------
@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email y password son obligatorios"}), 400

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify({
        "message": "Login correcto",
        "access_token": access_token,
        "user": user.serialize()
    }), 200

# ------------------------
# USERS
# ------------------------
@main.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.serialize() for u in users])

@main.route("/users", methods=["POST"])
@admin_required
def create_user():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password") or not data.get("name"):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "El email ya está registrado"}), 400

    user = User(
        name=data["name"],
        email=data["email"],
        role=data.get("role", "cliente"),
        image=data.get("image")
    )
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201

@main.route("/users/<int:user_id>", methods=["DELETE"])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado correctamente"}), 200

# ------------------------
# THERAPISTS
# ------------------------
@main.route("/therapists", methods=["GET"])
def get_therapists():
    therapists = Therapist.query.all()
    return jsonify([t.serialize() for t in therapists])

@main.route("/therapists", methods=["POST"])
@admin_required
def create_therapist():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("specialty"):
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    if Therapist.query.filter_by(name=data['name']).first():
        return jsonify({"error": "El terapeuta ya existe"}), 400
    th = Therapist(name=data['name'], specialty=data['specialty'], image=data.get('image'))
    db.session.add(th)
    db.session.commit()
    return jsonify(th.serialize()), 201

@main.route("/therapists/<int:therapist_id>", methods=["DELETE"])
@admin_required
def delete_therapist(therapist_id):
    th = Therapist.query.get_or_404(therapist_id)
    db.session.delete(th)
    db.session.commit()
    return jsonify({"message": "Terapeuta eliminado"}), 200

# ------------------------
# SERVICES
# ------------------------
@main.route("/services", methods=["GET"])
def get_services():
    services = Service.query.all()
    return jsonify([s.serialize() for s in services])

@main.route("/services", methods=["POST"])
@admin_required
def create_service():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("description"):
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    svc = Service(
        name=data['name'],
        description=data['description'],
        price=data.get('price', 0),
        duration=data.get('duration', 30),
        available=bool(data.get('available', True)),
        image=data.get('image')
    )
    db.session.add(svc)
    db.session.commit()
    return jsonify(svc.serialize()), 201

@main.route("/services/<int:service_id>", methods=["DELETE"])
@admin_required
def delete_service(service_id):
    svc = Service.query.get_or_404(service_id)
    db.session.delete(svc)
    db.session.commit()
    return jsonify({"message": "Servicio eliminado"}), 200

# ------------------------
# OFFERINGS (therapist <-> service)
# ------------------------
@main.route("/offerings", methods=["GET"])
def get_offerings():
    offerings = Offering.query.all()
    return jsonify([o.serialize() for o in offerings])

@main.route("/offerings", methods=["POST"])
@admin_required
def create_offering():
    data = request.get_json()
    if not data or not data.get("therapist_id") or not data.get("service_id") or not data.get("price"):
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    existing = Offering.query.filter_by(therapist_id=data['therapist_id'], service_id=data['service_id']).first()
    if existing:
        return jsonify({"error": "La oferta ya existe"}), 400
    off = Offering(
        therapist_id=data['therapist_id'],
        service_id=data['service_id'],
        price=data['price'],
        duration=data.get('duration', 30),
        available=bool(data.get('available', True))
    )
    db.session.add(off)
    db.session.commit()
    return jsonify(off.serialize()), 201

@main.route("/offerings/<int:offering_id>", methods=["DELETE"])
@admin_required
def delete_offering(offering_id):
    off = Offering.query.get_or_404(offering_id)
    db.session.delete(off)
    db.session.commit()
    return jsonify({"message": "Oferta eliminada"}), 200

# Obtener ofertas de un terapeuta
@main.route("/therapists/<int:therapist_id>/offerings", methods=["GET"])
def get_offerings_for_therapist(therapist_id):
    therapist = Therapist.query.get_or_404(therapist_id)
    return jsonify([o.serialize() for o in therapist.offerings])
