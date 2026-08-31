ZxZone-Master-MLTB: Ultimate Multi-Cloud Telegram Leech Bot
<p align="center"> <a href="https://github.com/obscure-n8/ZxZone-Master-MLTB"> <img src="https://graph.org/file/879239eb830dd6c00b07e.jpg" width="550" alt="ZxZone-Master-MLTB Logo"> </a> </p><p align="center"> <a href="https://github.com/obscure-n8/ZxZone-Master-MLTB/fork"> <img alt="Forks" src="https://img.shields.io/github/forks/obscure-n8/ZxZone-Master-MLTB?style=plastic&logo=git&color=orange&label=Forks"> </a> <a href="https://github.com/obscure-n8/ZxZone-Master-MLTB/stargazers"> <img alt="Stars" src="https://img.shields.io/github/stars/obscure-n8/ZxZone-Master-MLTB?style=plastic&logo=github&color=FFD700&label=Stars"> </a> </p><p align="center"> <a href="https://t.me/YourChannel"> <img alt="Telegram Channel" src="https://img.shields.io/badge/Join%20on%20Telegram%20Channel-0088CC?style=plastic&logo=telegram&logoColor=white&labelColor=0A3D62" width="250"> </a> </p>
⚡️ Download Anything. Upload Everywhere. 🔥
📌 Key Highlights
<details> <summary><strong>View All Highlights <kbd>Click Here</kbd></strong></summary>
ZxZone-Master-MLTB is a powerful and flexible multi-cloud Telegram leech bot designed for seamless file management.

🌐 Universal Downloader - Supports torrents, Mega, Google Drive, direct links, and all yt-dlp sites.

☁️ Cloud Uploader - Upload files to Google Drive, Telegram Cloud, Rclone, or DDL servers with ease.

📦 Smart File Handling - Automatic renaming, metadata tagging, and organization.

🧠 Intelligent Automation - Auto-resume, retry, and cleanup for 24×7 reliability.

⚙️ Advanced Controls - Manage downloads, uploads, and settings directly from Telegram (/bs, /mirror, /leech).

🎯 Multi-Deployment Ready - Deploy on Heroku, Docker, VPS, or Google Colab.

🔐 Secure & Private - Owner-only commands, user whitelisting, and access control.

💨 Lightweight Performance - Optimized Python & Pyrogram async engine for speed.

</details>
🚀 Deployment Guide (VPS)
<details> <summary><strong>View All Steps <kbd>Click Here</kbd></strong></summary>
1. Prerequisites
VPS with root access

Docker installed (optional)

Python 3.11+

2. Installing Requirements
Clone this repository:

bash
git clone https://github.com/obscure-n8/ZxZone-Master-MLTB
cd ZxZone-Master-MLTB
Setting up config file:

bash
cp config_sample.env config.env
Remove the first line saying:

text
_____REMOVE_THIS_LINE_____=True
Fill up rest of the fields.

NOTE: All values must be filled between quotes, even if it's Int, Bool or List.

3. Build and Run the Docker Image
Using Official Docker Commands
Build the Docker image:

bash
sudo docker build . -t zxzone
Run the image:

bash
sudo docker run -p 80:80 -p 8080:8080 zxzone
To stop the running container:

bash
sudo docker ps
sudo docker stop <container_id>
Using docker-compose (Recommended)
bash
sudo apt install docker-compose
sudo docker-compose up --build
</details>
🚀 Deployment Guide (Heroku)
<details> <summary><strong>View All Steps <kbd>Click Here</kbd></strong></summary>
Deploy Using Heroku CLI
Step 1: Git clone this Repo

bash
git clone https://github.com/obscure-n8/ZxZone-Master-MLTB
cd ZxZone-Master-MLTB
Step 2: Install Heroku CLI

bash
curl https://cli-assets.heroku.com/install.sh | sh
Step 3: Login to Heroku

bash
heroku login
Step 4: Create Heroku App

bash
heroku create --region us --stack container APP_NAME
Step 5: Set Config Vars in Heroku Dashboard or via CLI

bash
heroku config:set BOT_TOKEN="your_bot_token" -a APP_NAME
heroku config:set OWNER_ID="your_owner_id" -a APP_NAME
heroku config:set DATABASE_URL="your_mongodb_url" -a APP_NAME
heroku config:set BASE_URL="https://APP_NAME.herokuapp.com" -a APP_NAME
Step 6: Push to Heroku

bash
git push heroku main -f
Check Logs:

bash
heroku logs -a APP_NAME -t
</details>
🛠️ Variables Description
<details> <summary><b>View All Variables <kbd>Click Here</kbd></b></summary>
BOT_TOKEN: Telegram Bot Token from BotFather. Str

OWNER_ID: Telegram User ID of the bot owner. Int

TELEGRAM_API: API ID from https://my.telegram.org. Int

TELEGRAM_HASH: API Hash from https://my.telegram.org. Str

BASE_URL: Base URL for web file selection.

Heroku: https://APP_NAME.herokuapp.com

VPS: http://YOUR_IP:PORT

DATABASE_URL: MongoDB database URL. Str

UPSTREAM_REPO: GitHub repository URL for updates. Str

UPSTREAM_BRANCH: Upstream branch name. Default: main. Str

</details>
📝 Credits
Original Creator: anasty17

KPSML Modded by: Tamilupdates

WZML Modded by: SilentDemonSD

Merged & Enhanced by: AKJN

Repository Maintained by: obscure-n8

⚠️ Disclaimer
This bot is for educational purposes only. Users are responsible for their actions.

<p align="center"> <b>Made with ❤️ by Obscure & AKJN</b> </p>
