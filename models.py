from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Characteristic(db.Model):
    __tablename__ = 'characteristics'
    id = db.Column(db.Integer, primary_key=True)
    mushroom_id = db.Column(db.Integer, db.ForeignKey('mushrooms.id'), nullable=False)
    characteristic_name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Genus(db.Model):
    __tablename__ = 'genus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Mushroom(db.Model):
    __tablename__ = 'mushrooms'
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    substrate_id = db.Column(db.Integer, db.ForeignKey('substrates.id'), nullable=False)
    colonization_temp = db.Column(db.Float)
    avg_colonization_time = db.Column(db.Integer)
    fruiting_temp = db.Column(db.Float)
    avg_fruiting_time = db.Column(db.Integer)
    harvest_weight = db.Column(db.Float)
    color = db.Column(db.String(100))
    shape = db.Column(db.String(100))
    edibility = db.Column(db.String(100))
    name = db.Column(db.String(100), nullable=False)

class Observation(db.Model):
    __tablename__ = 'observations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mushroom_id = db.Column(db.Integer, db.ForeignKey('mushrooms.id'), nullable=False)
    observation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    photo_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    temperature = db.Column(db.Float)
    weather_conditions = db.Column(db.String(100))
    notes_tsvector = db.Column(db.Text)  # Assuming this is for full-text search; might need configuration.
    is_public = db.Column(db.Boolean, nullable=False, default=False)
    shared_with_users = db.Column(db.String(255))
    privacy_setting = db.Column(db.String(50), nullable=False, default='private')
    is_private = db.Column(db.Boolean, nullable=False, default=True)

class SpatialRefSys(db.Model):  # This seems to mirror a PostGIS table, ensure it's needed in your application context.
    __tablename__ = 'spatial_ref_sys'
    srid = db.Column(db.Integer, primary_key=True)
    auth_name = db.Column(db.String(256))
    auth_srid = db.Column(db.Integer)
    srtext = db.Column(db.String(2048))

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    genus_id = db.Column(db.Integer, db.ForeignKey('genus.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)

class Substrate(db.Model):
    __tablename__ = 'substrates'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    points = db.Column(db.Integer, default=0)
