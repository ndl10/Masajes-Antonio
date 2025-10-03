import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:password@localhost/centro_masajes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'clave_secreta_super_segura'  # Cambiar por algo seguro
