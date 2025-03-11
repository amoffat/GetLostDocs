import json
import os
import urllib.request
from datetime import datetime, timezone


def get_changes():
    try:
        with open("CHANGELOG.md", "r", encoding="utf-8") as f:
            lines = f.readlines()

        changelog = []
        in_section = False

        for line in lines:
            if line.startswith("## "):  # Start of a version section
                if in_section:
                    break  # Already collected the latest version block
                in_section = True
                continue

            if in_section:
                if line.strip():  # Skip empty lines
                    changelog.append(line.strip())

        return changelog if changelog else ["No changelog entries found."]
    except FileNotFoundError:
        return ["CHANGELOG.md not found."]


def send_notification():
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    docs_version = os.getenv("DOCS_VERSION")

    if not webhook_url or not docs_version:
        print("Missing DISCORD_WEBHOOK or DOCS_VERSION environment variables.")
        return

    changes = get_changes()
    fields = [
        {
            "name": "What’s New",
            "value": "\n".join(
                f"- {item.lstrip('-').strip()}" for item in changes[:10]
            ),
        }
    ]

    embed = {
        "title": f"📚 Docs v{docs_version} Deployed!",
        "url": f"https://docs.getlost.gg/{docs_version}/",
        "description": "A new version of the documentation is now live!",
        "color": 5814783,
        "fields": fields,
        "footer": {"text": "Github Deployment"},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    payload = {"embeds": [embed]}

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        webhook_url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Github Action",
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            print(f"Discord webhook sent successfully: {response.status}")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(
            f"""Failed to send Discord webhook. Status: {e.code}, \
            Response: {error_body}"""
        )


if __name__ == "__main__":
    send_notification()
