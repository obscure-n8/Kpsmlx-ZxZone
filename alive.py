import os
import time
import requests
from logging import error as logerror

HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', None)
PORT = os.environ.get('PORT', None)

BASE_URL = None
if HEROKU_APP_NAME:
    BASE_URL = f"https://{HEROKU_APP_NAME}.herokuapp.com"
elif PORT:
    BASE_URL = f"http://localhost:{PORT}"

if BASE_URL:
    while True:
        try:
            response = requests.get(BASE_URL, timeout=15)
            if response.status_code in:
                time.sleep(900)
            else:
                time.sleep(120)
        except Exception as e:
            logerror(f"Keep-alive network cycle bypass: {e}")
            time.sleep(300)
            continue
