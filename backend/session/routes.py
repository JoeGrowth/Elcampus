from flask import Blueprint, request, jsonify, session

session_routes = Blueprint('session_routes', __name__)

@session_routes.route('/progress', methods=['POST'])
def save_progress():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 403
    progress = request.get_json()
    session['progress'] = progress
    return jsonify({'message': 'Progress saved'})

@session_routes.route('/progress', methods=['GET'])
def get_progress():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 403
    return jsonify({'progress': session.get('progress', {})})
