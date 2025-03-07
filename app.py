from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

REPORTS_FILE = "reports.json"

# Load reports from JSON file
def load_reports():
    if not os.path.exists(REPORTS_FILE):
        return []
    with open(REPORTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save reports to JSON file
def save_reports(reports):
    with open(REPORTS_FILE, "w") as f:
        json.dump(reports, f, indent=4)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/report', methods=['POST'])
def submit_report():
    reports = load_reports()
    
    name = request.form.get("name", "Anonymous")
    bank = request.form.get("bank")
    issue = request.form.get("issue")
    details = request.form.get("details", "")

    if not bank or not issue:
        return render_template("error.html", message="Bank and Issue fields are required.")

    new_report = {
        "name": name,
        "bank": bank,
        "issue": issue,
        "details": details,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }

    reports.append(new_report)
    save_reports(reports)

    return render_template("success.html")

@app.route('/reports')
def reports():
    reports = load_reports()

    # No need to filter emails since they aren't saved anymore
    return render_template("reports.html", reports=reports)

if __name__ == '__main__':
    app.run(debug=True)
