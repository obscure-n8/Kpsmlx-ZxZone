#!/bin/bash

# Heroku check
if [[ -n $DYNO ]]; then
    echo "Running on Heroku"
    python3 update.py
fi

# Start bot
python3 -m bot
