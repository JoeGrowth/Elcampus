from flask import Blueprint, request, jsonify, session

auth = Blueprint('auth', __name__)
users = {}  # Simple in-memory user store

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = password
    return jsonify({'message': 'User registered'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        session['username'] = username
        session['progress'] = {}
        return jsonify({'message': 'Logged in'})
    return jsonify({'message': 'Invalid credentials'}), 401
