from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Initialisation des extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration de l'application
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['RECAPTCHA_SITE_KEY'] = os.getenv("RECAPTCHA_SITE_KEY")
    app.config['RECAPTCHA_SECRET_KEY'] = os.getenv("RECAPTCHA_SECRET_KEY")
    

    # Initialisation des extensions
    db.init_app(app)
    #migrate.init_app(app, db)

    # Enregistrement des routes (views)
    from app.routes.views_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


