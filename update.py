import os
import subprocess

UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO', 'https://github.com/obscure-n8/ZxZone-Master-MLTB')
UPSTREAM_BRANCH = os.environ.get('UPSTREAM_BRANCH', 'main')

if __name__ == "__main__":
    if os.path.exists('.git'):
        try:
            subprocess.run(["git", "fetch", "origin", UPSTREAM_BRANCH], check=True)
            subprocess.run(["git", "reset", "--hard", f"origin/{UPSTREAM_BRANCH}"], check=True)
        except Exception:
            pass
            
    subprocess.run(["pip3", "install", "--no-cache-dir", "-r", "requirements.txt"])
