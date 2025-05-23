
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
CORS(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = password
    return jsonify({'message': 'User registered'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        session['username'] = username
        session['progress'] = {}
        return jsonify({'message': 'Logged in'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/progress', methods=['POST'])
def save_progress():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 403
    progress = request.get_json()
    session['progress'] = progress
    return jsonify({'message': 'Progress saved'})

@app.route('/progress', methods=['GET'])
def get_progress():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 403
    return jsonify({'progress': session.get('progress', {})})

if __name__ == '__main__':
    app.run(debug=True)
