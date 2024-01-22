from flask import Blueprint, jsonify
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    file_path = './temp/data.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(file_path, 'w') as file:
            data = {'number': 0}
            json.dump(data, file)

    return jsonify(data)