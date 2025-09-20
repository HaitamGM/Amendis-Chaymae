from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db



class SiteGeographique(db.Model):
    __tablename__ = 'site_geographique'
    id_site = db.Column(db.Integer, primary_key=True)
    nom_site = db.Column(db.String(100))
    ville = db.Column(db.String(100))
    adresse = db.Column(db.String(200))
    tele = db.Column(db.String(20))

    utilisateurs = db.relationship('Utilisateur', backref='site', lazy=True)

class Direction(db.Model):
    __tablename__ = 'direction'
    id_direction = db.Column(db.Integer, primary_key=True)
    nom_direction = db.Column(db.String(100))
    tele_direction = db.Column(db.String(20))

    services = db.relationship('Service', backref='direction', lazy=True)
    utilisateurs = db.relationship('Utilisateur', backref='direction_ref', lazy=True)

class Service(db.Model):
    __tablename__ = 'service'
    id_service = db.Column(db.Integer, primary_key=True)
    id_direction = db.Column(db.Integer, db.ForeignKey('direction.id_direction'))
    nom_service = db.Column(db.String(100))

class Historique(db.Model):
    __tablename__ = 'historique'
    id_historique = db.Column(db.Integer, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id_utilisateur'))
    type_action = db.Column(db.String(100))
    date_action = db.Column(db.Date)
    description = db.Column(db.Text)

    utilisateur = db.relationship('Utilisateur', back_populates='historiques')
    materiels = db.relationship('Materiel', backref='historique_ref', lazy=True)

class Utilisateur(db.Model, UserMixin):
    __tablename__ = 'utilisateurs'
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    id_site = db.Column(db.Integer, db.ForeignKey('site_geographique.id_site'))
    id_direction = db.Column(db.Integer, db.ForeignKey('direction.id_direction'))
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(128), nullable=False)
    tele = db.Column(db.String(20))
    adresse = db.Column(db.String(100))
    role= db.Column(db.String(10))
    
    historiques = db.relationship('Historique', back_populates='utilisateur')
    demandes = db.relationship('DemandeIntervention', backref='utilisateur', lazy=True)
    materiels = db.relationship('Materiel', backref='utilisateur_ref', lazy=True)

class DemandeIntervention(db.Model):
    __tablename__ = 'demande_interventions'
    id_demande = db.Column(db.Integer, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id_utilisateur'))
    objet = db.Column(db.String(200))
    description = db.Column(db.Text)
    date_demande = db.Column(db.Date)
    statut = db.Column(db.String(50))
    priorite = db.Column(db.String(50))
    type_d_intervention = db.Column(db.String(100))

    materiels = db.relationship('Materiel', backref='demande_ref', lazy=True)

class Materiel(db.Model):
    __tablename__ = 'materiels'
    id_materiels = db.Column(db.Integer, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id_utilisateur'))
    id_historique = db.Column(db.Integer, db.ForeignKey('historique.id_historique'))
    id_demande = db.Column(db.Integer, db.ForeignKey('demande_interventions.id_demande'))
    N_serie = db.Column(db.String(100))
    N_inventaire = db.Column(db.String(100))
    type = db.Column(db.String(100))
    modele = db.Column(db.String(100))
    marque = db.Column(db.String(100))
    etat = db.Column(db.String(50))
    date_achat = db.Column(db.Date)
    date_affectation = db.Column(db.Date)
    garantie = db.Column(db.String(100))
    Periode_anciennete = db.Column(db.String(100))

    caracteristiques = db.relationship('Caracteristique', backref='materiel', lazy=True)

class Caracteristique(db.Model):
    __tablename__ = 'caracteristique'
    id_caracteristique = db.Column(db.Integer, primary_key=True)
    id_materiels = db.Column(db.Integer, db.ForeignKey('materiels.id_materiels'))
    nom_caracteristique = db.Column(db.String(100))
    valeur = db.Column(db.String(200))

