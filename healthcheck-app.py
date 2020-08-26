import os
import environ
import urllib.request
import sys

env = environ.Env()
if 'ENV_PATH' in os.environ:
    environ.Env.read_env(os.environ['ENV_PATH'])

try:
    urllib.request.urlopen("http://localhost:8000/", timeout=10)
except Exception:
    sys.exit(1)
else:
    if env('APP_HEALTHCHECK_URL', default=None):
        try:
            urllib.request.urlopen(env('APP_HEALTHCHECK_URL'), timeout=10)
        except Exception:
            pass
sys.exit(0)
