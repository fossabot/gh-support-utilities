from flask import Flask, request, jsonify
import requests

app = Flask(__name)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Verify the webhook secret here if you've set one.

    payload = request.json
    if payload["action"] == "created":
        new_repo_name = payload["repository"]["name"]
        issue_template_repo = "gh-support-utilities"
        issue_template = "new-repo-issue.md"
        token = "YOUR_PERSONAL_ACCESS_TOKEN"

        issue_content = requests.get(f"https://raw.githubusercontent.com/{issue_template_repo}/master/{issue_template}").text

        issue_data = {
            "title": "Your Issue Title",
            "body": issue_content
        }

        issue_url = f"https://api.github.com/repos/{new_repo_name}/issues"
        response = requests.post(issue_url, json=issue_data, headers={"Authorization": f"token {token}"})

        if response.status_code == 201:
            return "Issue created successfully."
        else:
            return "Failed to create issue."

if __name__ == "__main__":
    app.run(debug=True)
