
import os.path

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        # You can swap out the engine for MySQL easily by changing this value
        # to ``django.db.backends.mysql`` or to PostgreSQL with
        # ``django.db.backends.postgresql_psycopg2``

        # If you change this, you'll also need to install the appropriate python
        # package: psycopg2 (Postgres) or mysql-python
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'sentry',
        'USER': 'sentry',
        'PASSWORD': 'sentry',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# If you're expecting any kind of real traffic on Sentry, we highly recommend configuring
# the CACHES and Redis settings

CACHES = {
     'default': {
         'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
         'LOCATION': ['127.0.0.1:11211'],
     }
}

# Buffers (combined with queueing) act as an intermediate layer between the database and
# the storage API. They will greatly improve efficiency on large numbers of the same events
# being sent to the API in a short amount of time.

# SENTRY_USE_QUEUE = True
# For more information on queue options, see the documentation for Celery:
# http://celery.readthedocs.org/en/latest/
# BROKER_URL = 'redis://localhost:6379'

# SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
# SENTRY_BUFFER_OPTIONS = {
#     'hosts': {
#         0: {
#             'host': '127.0.0.1',
#             'port': 6379,
#         }
#     }
# }


SENTRY_KEY = '{{secret_key}}'

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
SENTRY_URL_PREFIX = '{{root_url}}'  # No trailing slash!

SENTRY_WEB_HOST = '127.0.0.1'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = '{{server_email}}'
EMAIL_HOST = '{{smtp_server}}'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = '1042684111028.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'tUNMns4mfL4Fb7zLJ3byskLj'

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
