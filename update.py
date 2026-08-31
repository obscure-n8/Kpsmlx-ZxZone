# update.py - ZxZone-Master-MLTB Custom
import os
import subprocess
import sys

UPSTREAM_REPO = "https://github.com/obscure-n8/ZxZone-Master-MLTB"
UPSTREAM_BRANCH = "main"

if __name__ == "__main__":
    # Pull latest changes without overwriting existing files
    if not os.path.exists('.git'):
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "remote", "add", "origin", UPSTREAM_REPO])
        subprocess.run(["git", "fetch", "origin", UPSTREAM_BRANCH])
        subprocess.run(["git", "reset", "--hard", f"origin/{UPSTREAM_BRANCH}"])
    else:
        subprocess.run(["git", "fetch", "origin", UPSTREAM_BRANCH])
        subprocess.run(["git", "reset", "--hard", f"origin/{UPSTREAM_BRANCH}"])
    
    # Reinstall requirements if needed
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
