from flask import Blueprint, request, jsonify, session

journey_bp = Blueprint('journey', __name__)

# Sample episode logic
ROLE_EPISODES = {
    "to design": ["Episode 1: Define Vision", "Episode 2: Build Design System"],
    "to secure": ["Episode 1: Identify Leads", "Episode 2: Sales Pitch System"]
}

@journey_bp.route('/api/start-journey', methods=['POST'])
def start_journey():
    name = request.form.get('name')
    role = request.form.get('role').strip().lower()

    if not name or not role:
        return jsonify({"result": "error", "message": "Missing name or role"}), 400

    episodes = ROLE_EPISODES.get(role, ["Episode 1: Custom Journey Coming Soon"])

    # Store in session (or later: DB)
    session['user'] = {
        "name": name,
        "role": role,
        "episodes": episodes
    }

    return jsonify({
        "result": "success",
        "name": name,
        "role": role,
        "episodes": episodes
    })
