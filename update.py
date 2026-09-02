import os

def update_repo():
    os.system("git fetch --all")
    os.system("git reset --hard origin/main")
    os.system("pip install --upgrade -r requirements.txt")

if __name__ == "__main__":
    update_repo()
