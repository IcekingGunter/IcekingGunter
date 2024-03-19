from flask import Blueprint, jsonify, request, Blueprint
from mycologyflask import db, Mushroom  # Import necessary models
from datetime import datetime
from mycologyflask.models import Mushroom

# Create a blueprint object for mushrooms routes
mushrooms_bp = Blueprint('mushrooms', __name__)

# Route to get all mushrooms
@mushrooms_bp.route('/mushrooms', methods=['GET'])
def get_mushrooms():
    mushrooms = Mushroom.query.all()
    mushroom_list = [{'id': m.id, 'species_id': m.species_id, 'name': m.name} for m in mushrooms]
    return jsonify(mushroom_list)

# Route to get a specific mushroom by ID
@mushrooms_bp.route('/mushrooms/<int:mushroom_id>', methods=['GET'])
def get_mushroom(mushroom_id):
    mushroom = Mushroom.query.get_or_404(mushroom_id)
    return jsonify({'id': mushroom.id, 'species_id': mushroom.species_id, 'name': mushroom.name})

# Route to create a new mushroom
@mushrooms_bp.route('/mushrooms', methods=['POST'])
def create_mushroom():
    data = request.json
    new_mushroom = Mushroom(species_id=data['species_id'], name=data['name'])
    db.session.add(new_mushroom)
    db.session.commit()
    return jsonify({'message': 'Mushroom created successfully'}), 201

# Route to update an existing mushroom
@mushrooms_bp.route('/mushrooms/<int:mushroom_id>', methods=['PUT'])
def update_mushroom(mushroom_id):
    mushroom = Mushroom.query.get_or_404(mushroom_id)
    data = request.json
    mushroom.species_id = data['species_id']
    mushroom.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Mushroom updated successfully'})

# Route to delete an existing mushroom
@mushrooms_bp.route('/mushrooms/<int:mushroom_id>', methods=['DELETE'])
def delete_mushroom(mushroom_id):
    mushroom = Mushroom.query.get_or_404(mushroom_id)
    db.session.delete(mushroom)
    db.session.commit()
    return jsonify({'message': 'Mushroom deleted successfully'})
