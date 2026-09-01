#!/bin/bash
if [[ -n $DYNO ]]; then
    echo "Running on Heroku"
    python3 update.py
fi
python3 -m bot
