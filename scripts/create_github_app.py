#!/usr/bin/env python3
"""
Creates a GitHub App for workflow automation across agentivo repos.
"""

import signal
import sys
import webbrowser
from urllib.parse import quote


def handle_sigint(_sig, _frame):
    print("\n\nCancelled.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

ORG = "agentivo"
APP_NAME = "Agentivo Integrations"
HOMEPAGE = "https://github.com/agentivo"
DESCRIPTION = "Workflow automation for agentivo repos"

PERMISSIONS = {
    "actions": "write",
    "contents": "read",
    "organization_models": "read",
}


def main():
    print(f"Creating GitHub App: {APP_NAME}\n")

    print("Configuration:")
    print(f"  Name:        {APP_NAME}")
    print(f"  Org:         {ORG}")
    print(f"  Description: {DESCRIPTION}")
    print(f"  Webhook:     Disabled")
    print()
    print("Permissions:")
    for perm, level in PERMISSIONS.items():
        print(f"  {perm}: {level}")
    print()

    input("Press Enter to open browser...")

    query_parts = [
        f"name={quote(APP_NAME)}",
        f"description={quote(DESCRIPTION)}",
        f"url={quote(HOMEPAGE, safe='')}",
        "webhook_active=false",
        "public=false",
    ] + [f"{perm}={level}" for perm, level in PERMISSIONS.items()]

    # Create under org settings
    github_url = f"https://github.com/organizations/{ORG}/settings/apps/new?" + "&".join(query_parts)

    webbrowser.open(github_url)

    print("\nAfter creating the app:")
    print("1. Copy the App ID from the app settings page")
    print("2. Scroll down and click 'Generate a private key'")
    print("3. Install the app on agentivo repos (left sidebar -> Install App)")
    print("4. For each repo that needs auto-restart, add secrets:")
    print()
    print("   gh secret set APP_ID -R agentivo/REPO_NAME")
    print("   gh secret set APP_PRIVATE_KEY -R agentivo/REPO_NAME < ~/Downloads/*.pem")


if __name__ == "__main__":
    main()
