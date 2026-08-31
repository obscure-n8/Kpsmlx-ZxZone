# update.py - ZxZone-Master-MLTB Custom
from os import path as ospath
from subprocess import run as srun
from logging import info as log_info, error as log_error

UPSTREAM_REPO = "https://github.com/obscure-n8/ZxZone-Master-MLTB"
UPSTREAM_BRANCH = "main"

if __name__ == "__main__":
    if not ospath.exists('.git'):
        srun(["git", "init", "-q"])
        srun(["git", "remote", "add", "origin", UPSTREAM_REPO])
        srun(["git", "fetch", "origin", UPSTREAM_BRANCH])
        srun(["git", "reset", "--hard", f"origin/{UPSTREAM_BRANCH}"])
        log_info("Initial clone completed!")
    else:
        srun(["git", "fetch", "origin", UPSTREAM_BRANCH])
        srun(["git", "reset", "--hard", f"origin/{UPSTREAM_BRANCH}"])
        log_info("Updated with latest commits!")
