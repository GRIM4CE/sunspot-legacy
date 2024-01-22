from flask import Blueprint, jsonify
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    with open('./temp/data.json', 'r') as file:
        data = json.load(file)

    return jsonify(data)