#!/bin/bash
set -e

python3 alive.py &

exec python3 -m bot
