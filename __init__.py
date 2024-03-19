from flask import Blueprint
from .mushrooms import mushrooms_bp  # Ensure this import is correct based on your file structure

def register_routes(app: Flask):
    app.register_blueprint(mushrooms_bp, url_prefix='/mushrooms')
