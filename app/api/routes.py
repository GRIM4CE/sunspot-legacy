from flask import Blueprint, jsonify
from app.db import get_sunspot, drop_records
from bson import json_util

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET'])
def index():
    try:
        data_list = get_sunspot()
        response_json = json_util.dumps(data_list)
        return jsonify(response_json)
    except ():
        print("error")
        


@api_bp.route('/drop', methods=['GET'])
def drop_records_route():
    try:
        deleted_count = drop_records()
        return f"Deleted {deleted_count} records."
    except Exception as e:
        return f"Error: {str(e)}"