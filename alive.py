from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror

BASE_URL = environ.get('BASE_URL', None)
PORT = environ.get('PORT', None)
DYNO = environ.get('DYNO', None)

if BASE_URL is None or len(BASE_URL) == 0:
    BASE_URL = None
else:
    BASE_URL = BASE_URL.rstrip("/")

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
