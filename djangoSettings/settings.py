import os
import django_heroku
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'secret_key'

DEBUG = False

ALLOWED_HOSTS = ['*']


AUTH_USER_MODEL = ''

