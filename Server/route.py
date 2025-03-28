from flask import Blueprint, request, jsonify
from model import search_company

api_bp = Blueprint('api', __name__)

@api_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = search_company(query)
    return jsonify(results)
