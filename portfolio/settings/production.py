from portfolio.settings.base import *
from portfolio.utils.settings import get_env_variable
import os, dj_database_url
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '') == 'False'

# Whitenoise Middleware
MIDDLEWARE.insert(2, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES['default'] = dj_database_url.parse(
    os.environ.get('DATABASE_URL'), conn_max_age=600
)


CSRF_COOKIE_SECURE = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'assets'