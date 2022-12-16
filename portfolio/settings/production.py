from portfolio.settings.base import *
from portfolio.utils.settings import get_env_variable
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable("DEBUG", "True")

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES['default'] ={
    'ENGINE': get_env_variable("DB_ENGINE"),
    'NAME': get_env_variable("DB_NAME"),
    'USER': get_env_variable("DB_USER"),
    'PASSWORD': get_env_variable("DB_PASSWORD"),
    'HOST': get_env_variable("DB_HOST"),
    'PORT': ''
}