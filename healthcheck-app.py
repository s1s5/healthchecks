import os
import sys
import urllib.request

APP_HEALTHCHECK_URL = os.getenv("APP_HEALTHCHECK_URL")

try:
    urllib.request.urlopen("http://localhost:8000/", timeout=10)
except Exception:
    sys.exit(1)
else:
    if APP_HEALTHCHECK_URL:
        try:
            urllib.request.urlopen(APP_HEALTHCHECK_URL, timeout=10)
        except Exception:
            pass
sys.exit(0)
