import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

EXERCISES = [
    {"id": "jumping_jack", "name": "Jumping Jack", "default_target": 10, "emoji": "⭐"},
    {"id": "squat", "name": "Squat", "default_target": 15, "emoji": "🦵"},
    {"id": "lunge", "name": "Lunge", "default_target": 10, "emoji": "🏃"},
]

@app.route("/")
def index():
    return render_template("index.html", exercises=EXERCISES)

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "system": "LearnGate Exercise Counter",
        "pose_engine": "Browser MediaPipe Tasks Vision",
        "python_mediapipe_required": False,
        "exercises": EXERCISES,
    })

@app.route("/api/exercises")
def exercises():
    return jsonify({"exercises": EXERCISES})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
