#!/bin/bash
set -e

# Start alive server
python3 alive.py &

# Run bot
exec python3 bot.py
