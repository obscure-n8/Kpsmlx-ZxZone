from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror

PORT = environ.get('PORT', None)
DYNO = environ.get('DYNO', None)
HEROKU_APP_NAME = environ.get('HEROKU_APP_NAME', None)

BASE_URL = None

if DYNO is not None and HEROKU_APP_NAME is not None:
    BASE_URL = f"https://{HEROKU_APP_NAME}.herokuapp.com"

if DYNO is not None and BASE_URL is not None:
    while True:
        try:
            response = rget(BASE_URL, timeout=10)
            if response.status_code == 200:
                sleep(600)
            else:
                sleep(30)
        except Exception as e:
            logerror(f"Keep-alive error: {e}")
            sleep(60)
            continue
