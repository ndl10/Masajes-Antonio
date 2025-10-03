from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from routes import main
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "mydatabase.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_SECRET_KEY'] = 'clave_secreta_super_segura'

jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main, url_prefix="/api")

@app.route("/")
def home():
    return jsonify({"message": "API Flask funcionando correctamente con SQLite y JWT"})

if __name__ == "__main__":
    app.run(debug=True)
