from flask import Flask
from flask_cors import CORS
from flask_session import Session

from auth.routes import auth
from session.routes import session_routes

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
CORS(app)

# Register Blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(session_routes, url_prefix='/session')

if __name__ == '__main__':
    app.run(debug=True)
