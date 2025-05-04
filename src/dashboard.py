from flask import Flask, render_template
import os
from main import score_config, load_config

app = Flask(__name__)

@app.route("/")
def home():
    # Build path to sample_config.json
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    config_path = os.path.join(project_root, "demo", "sample_config.json")

    config = load_config(config_path)
    if not config:
        return "<h1>Error loading config file</h1>"

    # Get score and findings
    score, findings = score_config(config)

    # Set color class
    if score >= 80:
        score_class = "good"
    elif score >= 60:
        score_class = "warn"
    else:
        score_class = "bad"

    return render_template("score.html", score=score, score_class=score_class, findings=findings)

if __name__ == "__main__":
    app.run(debug=True)
