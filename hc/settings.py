"""
Django settings for healthchecks project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings
"""

import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
if 'ENV_PATH' in os.environ:
    environ.Env.read_env(os.environ['ENV_PATH'])


SECRET_KEY = env("SECRET_KEY", default="secret_key")
METRICS_KEY = env("METRICS_KEY", default="metrics_key")
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL",
                         default="healthchecks@example.org")
SUPPORT_EMAIL = env("SUPPORT_EMAIL", default="info@example.com")
USE_PAYMENTS = env.bool("USE_PAYMENTS", default=False)
REGISTRATION_OPEN = env.bool("REGISTRATION_OPEN", default=True)

VERSION = ""
with open(os.path.join(BASE_DIR, "CHANGELOG.md"), encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith("## v"):
            VERSION = line.split()[1]
            break


INSTALLED_APPS = (
    "hc.accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "hc.api",
    "hc.front",
    "hc.payments",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "hc.accounts.middleware.TeamAccessMiddleware",
]

AUTHENTICATION_BACKENDS = (
    "hc.accounts.backends.EmailBackend",
    "hc.accounts.backends.ProfileBackend",
)

ROOT_URLCONF = "hc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "hc.front.context_processors.branding",
                "hc.payments.context_processors.payments",
            ]
        },
    }
]

WSGI_APPLICATION = "hc.wsgi.application"
TEST_RUNNER = "hc.api.tests.CustomRunner"


DATABASES = {
    "default": env.db(default="sqlite:///hc.sqlite"),
}

USE_TZ = True
TIME_ZONE = env("TIME_ZONE", default="Asia/Tokyo")
LANGUAGE_CODE = env("LANGUAGE_CODE", default="ja")
USE_I18N = True
USE_L10N = True
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

SITE_ROOT = env("SITE_ROOT", default="http://localhost:8000")
SITE_NAME = env("SITE_NAME", default="Mychecks")
MASTER_BADGE_LABEL = env("MASTER_BADGE_LABEL", default=SITE_NAME)
PING_ENDPOINT = env("PING_ENDPOINT", default=SITE_ROOT + "/ping/")
PING_EMAIL_DOMAIN = env("PING_EMAIL_DOMAIN", default="localhost")
PING_BODY_LIMIT = env.int("PING_BODY_LIMIT", default=10000)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = env("STATIC_ROOT", default=os.path.join(BASE_DIR, "static-collected"))
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)
COMPRESS_OFFLINE = True
COMPRESS_CSS_HASHING_METHOD = "content"


# Discord integration
DISCORD_CLIENT_ID = env("DISCORD_CLIENT_ID", default=None)
DISCORD_CLIENT_SECRET = env("DISCORD_CLIENT_SECRET", default=None)

# Email integration
vars().update(env.email_url('EMAIL_URL', default='consolemail://'))

# Slack integration
SLACK_CLIENT_ID = env("SLACK_CLIENT_ID", default=None)
SLACK_CLIENT_SECRET = env("SLACK_CLIENT_SECRET", default=None)

# Pushover integration
PUSHOVER_API_TOKEN = env("PUSHOVER_API_TOKEN", default=None)
PUSHOVER_SUBSCRIPTION_URL = env("PUSHOVER_SUBSCRIPTION_URL", default=None)
PUSHOVER_EMERGENCY_RETRY_DELAY = env.int("PUSHOVER_EMERGENCY_RETRY_DELAY", default=300)
PUSHOVER_EMERGENCY_EXPIRATION = env.int("PUSHOVER_EMERGENCY_EXPIRATION", default=86400)

# Pushbullet integration
PUSHBULLET_CLIENT_ID = env("PUSHBULLET_CLIENT_ID", default=None)
PUSHBULLET_CLIENT_SECRET = env("PUSHBULLET_CLIENT_SECRET", default=None)

# Telegram integration -- override in local_settings.py
TELEGRAM_BOT_NAME = env("TELEGRAM_BOT_NAME", default="ExampleBot")
TELEGRAM_TOKEN = env("TELEGRAM_TOKEN", default=None)

# SMS and WhatsApp (Twilio) integration
TWILIO_ACCOUNT = env("TWILIO_ACCOUNT", default=None)
TWILIO_AUTH = env("TWILIO_AUTH", default=None)
TWILIO_FROM = env("TWILIO_FROM", default=None)
TWILIO_USE_WHATSAPP = env.bool("TWILIO_USE_WHATSAPP", default=False)

# PagerDuty
PD_VENDOR_KEY = env("PD_VENDOR_KEY", default=None)

# Trello
TRELLO_APP_KEY = env("TRELLO_APP_KEY", default=None)

# Matrix
MATRIX_HOMESERVER = env("MATRIX_HOMESERVER", default=None)
MATRIX_USER_ID = env("MATRIX_USER_ID", default=None)
MATRIX_ACCESS_TOKEN = env("MATRIX_ACCESS_TOKEN", default=None)

# Apprise
APPRISE_ENABLED = env.bool("APPRISE_ENABLED", default=False)

# Local shell commands
SHELL_ENABLED = env.bool("SHELL_ENABLED", default=False)

SESSION_COOKIE_NAME = env('SESSION_COOKIE_NAME', default='sessionid')
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
CACHES = {
    'default': env.cache(default='memcache://'),
}


if env.bool('USE_WHITENOISE', default=False):
    MIDDLEWARE.insert(
        MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1,
        'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    COMPRESS_ENABLED = False

if env('SENTRY_DSN', default=None):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=env('SENTRY_DSN'),
        integrations=[DjangoIntegration()],
        send_default_pii=True
    )

SENDALERTS_HEALTHCHECK_URL = env('SENDALERTS_HEALTHCHECK_URL', default=None)
