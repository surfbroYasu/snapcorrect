from .base import *
import os

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = str(os.environ.get("DEBUG"))=="1" #1 being True
# Change Debug setting by changing number preferably to "0" for DEBUG=False

PRODUCTION = str(os.environ.get("PRODUCTION"))=="0" #1 being True
# This is a dev setting defult PRODUCTION = "0" being false

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    'localhost:8000'
    # ...
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# POSTGRES_DB = os.getenv("POSTGRES_DB")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
# POSTGRES_USER = os.getenv("POSTGRES_USER")
# POSTGRES_HOST = os.getenv("POSTGRES_HOST")
# POSTGRES_PORT = os.getenv("POSTGRES_PORT")

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": POSTGRES_DB,
#         "USER": POSTGRES_USER,
#         "PASSWORD": POSTGRES_PASSWORD,
#         "HOST": POSTGRES_HOST,
#         "PORT": POSTGRES_PORT,
#     }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
    # BASE_DIR / "media",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = 'snapcorrect'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    # media file management
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
        },
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
        },
}


# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'SnapCorrect'
ACCOUNT_EMAIL_PREFIX = ''