"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from email.policy import default
from pathlib import Path
from os import path
import dj_database_url
import sys
sys.modules['django.utils.six.moves.urllib.parse'] = __import__('six.moves.urllib_parse', fromlist=['urlencode'])
sys.modules['django.utils.six.moves.urllib.request'] = __import__('six.moves.urllib_request', fromlist=['urlopen'])


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wi@alc3$i&lzrp#ky5lgt0nho2tyqlmuwqvfjkr+ok9@b!clmp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOST = ['127.0.0.1', '*.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo',
    'accounts',
    'disqus',
    'django.contrib.sites',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'config.urls'

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# reverse_lazy 함수를 사용해서 다른 뷰를 적용할 수 있다
# settings.py에서는 항상 lazy를 사용해야 함
LOGIN_REDIRECT_URL='/'


# disqus 설정
DISQUS_WEBSITE_SHORTNAME = 'dstargram-poqw'
SITE_ID = 1

# AWS S3적용
AWS_ACCESS_KEY_ID = 'AKIASHFOPX55OEE7YIGQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'dstargram'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' %(AWS_STORAGE_BUCKET_NAME, AWS_REGION)

AWS_S3_FILE_OVERWRITE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl' : 'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'

# static저장소 연결
STATIC_URL = 'http://%s/%s/' %(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# media저장소 연결(boto3 오버라이드)
MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'config.s3media.MediaStorage'

