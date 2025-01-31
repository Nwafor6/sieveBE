import os
from pathlib import Path
from urllib.parse import urlparse
from datetime import timedelta
import environ
import dj_database_url


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    APP_ENV=(str, False),
)

environ.Env.read_env()


import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9x8lwknby@t+0sk1v3m3u&^&@lxr7-5l&xy7#&5elhw43a!c9x"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
APP_ENV = env("APP_ENV", default="production")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mainapp",
    "rest_framework",
    "corsheaders",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "project.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"
CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# settings.py

# Static files (CSS, JavaScript, Images)
# STATIC_URL = "/static/"

# if APP_ENV in ["dev", "prod"]:
#     # Use AWS S3 for static and media files in 'dev' and 'prod' environments
#     MEDIA_URL = "media/"
#     MEDIA_ROOT = BASE_DIR / "media"

#     STATIC_URL = "static/"
#     STATICFILES_DIRS = [BASE_DIR / "static"]  # Directory for development static files

#     AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
#     AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
#     AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
#     AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
#     AWS_S3_FILE_OVERWRITE = False

#     # Django-storages settings
#     STORAGES = {
#         "default": {
#             "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         },
#         "staticfiles": {
#             "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         },
#     }

# else:
#     # Use local file system for static and media files in 'local' environment
#     MEDIA_URL = "/media/"
#     MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # Directory for uploaded files

#     STATIC_URL = "/static/"
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, "static")
#     ]  # Directory for development static files
#     STATIC_ROOT = os.path.join(
#         BASE_DIR, "staticfiles"
#     )  # Directory for collected static files in production


# settings.py

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

if APP_ENV in ["dev", "prod"]:
    # Use AWS S3 for media files in 'dev' and 'prod' environments
    MEDIA_URL = (
        f"https://{os.getenv('AWS_STORAGE_BUCKET_NAME')}.s3.amazonaws.com/media/"
    )
    MEDIA_ROOT = BASE_DIR / "media"

    # Use local file system for static files
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [BASE_DIR / "static"]  # Directory for development static files
    STATIC_ROOT = os.path.join(
        BASE_DIR, "staticfiles"
    )  # Directory for collected static files

    # AWS S3 configuration
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_FILE_OVERWRITE = False

    # Django-storages settings
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # Media files go to S3
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",  # Static files go to local file system
        },
    }

else:
    # Use local file system for static and media files in 'local' environment
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # Directory for uploaded files

    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]  # Directory for development static files
    STATIC_ROOT = os.path.join(
        BASE_DIR, "staticfiles"
    )  # Directory for collected static files in production

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
