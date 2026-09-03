#!/bin/bash
set -e

# Sync/update config before starting (if you have this step)
python3 update.py

# Start alive server in background (keeps port bound for Heroku)
python3 alive.py &

# Run the bot as a package (NOT bot.py, since bot/ is a folder)
exec python3 -m bot
