ZxZone-Master-MLTB: Ultimate Multi-Cloud Telegram Leech Bot
<h1 align="center">⚡ ZxZone-Master-MLTB ⚡</h1> <h3 align="center">Download Anything. Upload Everywhere. 🔥</h3><p align="center"> <a href="https://github.com/obscure-n8/ZxZone-Master-MLTB/fork"> <img alt="Forks" src="https://img.shields.io/github/forks/obscure-n8/ZxZone-Master-MLTB?style=plastic&logo=git&color=orange&label=Forks"> </a> <a href="https://github.com/obscure-n8/ZxZone-Master-MLTB/stargazers"> <img alt="Stars" src="https://img.shields.io/github/stars/obscure-n8/ZxZone-Master-MLTB?style=plastic&logo=github&color=FFD700&label=Stars"> </a> <a href="https://github.com/obscure-n8/ZxZone-Master-MLTB/issues"> <img alt="Issues" src="https://img.shields.io/github/issues/obscure-n8/ZxZone-Master-MLTB?style=plastic&logo=github&color=red&label=Issues"> </a> </p>
📌 Key Features
<details> <summary><strong>Click to View All Features</strong></summary>
ZxZone-Master-MLTB is a powerful multi-cloud Telegram leech bot with advanced features.

Feature	Description
🌐 Universal Downloader	Supports torrents, Mega, Google Drive, direct links, and all yt-dlp sites
☁️ Cloud Uploader	Upload to Google Drive, Telegram Cloud, Rclone, or DDL servers
📦 Smart File Handling	Auto-rename, metadata tagging, and organization
🧠 Intelligent Automation	Auto-resume, retry, and cleanup for 24×7 reliability
⚙️ Advanced Controls	Manage via Telegram commands: /bs, /mirror, /leech
🎯 Multi-Deployment	Deploy on Heroku, Docker, VPS, or Google Colab
🔐 Secure & Private	Owner-only commands and user whitelisting
💨 Lightweight Performance	Optimized Python & Pyrogram async engine
</details>
🚀 Quick Deployment
<details> <summary><strong>VPS Deployment</strong></summary>
Prerequisites
VPS with root access

Docker (optional)

Python 3.11+

Installation
bash
git clone https://github.com/obscure-n8/ZxZone-Master-MLTB
cd ZxZone-Master-MLTB
cp config_sample.env config.env
Edit config.env and remove _____REMOVE_THIS_LINE_____=True

Docker Deployment
bash
sudo docker build . -t zxzone
sudo docker run -p 80:80 -p 8080:8080 zxzone
Docker Compose
bash
sudo apt install docker-compose
sudo docker-compose up --build
</details><details> <summary><strong>Heroku Deployment</strong></summary>
Heroku CLI Method
bash
git clone https://github.com/obscure-n8/ZxZone-Master-MLTB
cd ZxZone-Master-MLTB
heroku login
heroku create --region us --stack container APP_NAME
heroku config:set BOT_TOKEN="your_bot_token" -a APP_NAME
heroku config:set OWNER_ID="your_owner_id" -a APP_NAME
heroku config:set DATABASE_URL="your_mongodb_url" -a APP_NAME
heroku config:set BASE_URL="https://APP_NAME.herokuapp.com" -a APP_NAME
git push heroku main -f
Check Logs
bash
heroku logs -a APP_NAME -t
</details>
🛠️ Configuration Variables
<details> <summary><strong>View All Variables</strong></summary>
Variable	Description	Type
BOT_TOKEN	Telegram Bot Token from BotFather	Str
OWNER_ID	Telegram User ID of bot owner	Int
TELEGRAM_API	API ID from my.telegram.org	Int
TELEGRAM_HASH	API Hash from my.telegram.org	Str
BASE_URL	Base URL for web selection (Heroku: https://APP_NAME.herokuapp.com, VPS: http://YOUR_IP:PORT)	Str
DATABASE_URL	MongoDB connection string	Str
UPSTREAM_REPO	GitHub repo URL for updates	Str
UPSTREAM_BRANCH	Branch name (default: main)	Str
</details>
📝 Credits
Contributor	Role
anasty17	Original Creator
Tamilupdates	KPSML Mod
SilentDemonSD	WZML Mod
obscure-n8	Merged, Enhanced & Maintained
⚠️ Disclaimer
text
This bot is for educational purposes only.
Users are responsible for their actions.
The developers are not liable for any misuse.
⭐ Support
If you like this project, please give it a star ⭐

<p align="center"> <b>Made with ❤️ by Obscure </b> </p>
