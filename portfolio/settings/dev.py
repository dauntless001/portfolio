from portfolio.settings.base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-b6e0i+#*0r3t9o$j0%sho=k$ka&ds6!4cw+(289#f5+3%5*f$2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES['default'] ={
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}