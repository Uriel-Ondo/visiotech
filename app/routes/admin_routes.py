# Fichier dédié aux fonctions administratives
from app import db
from app.models import Service

def add_service(name, description, price):
    service = Service(name=name, description=description, price=price)
    db.session.add(service)
    db.session.commit()

def delete_service(service_id):
    service = Service.query.get(service_id)
    if service:
        db.session.delete(service)
        db.session.commit()
