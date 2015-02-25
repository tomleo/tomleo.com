"""
Django settings for tomleo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJ_DIR = os.path.abspath(os.path.join(BASE_DIR, '../config'))

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

conf_settings = None
with open(os.path.join(PROJ_DIR, 'secrets.yml'), 'r') as f:
    conf_settings = load(f, Loader=Loader)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^(-nij=d#m*m#v6amu_g5=_4qkf%9=n50*^gapwr6m@fhwm#qp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = conf_settings.get('installed_apps')
MIDDLEWARE_CLASSES = conf_settings.get('middleware_classes')

ROOT_URLCONF = 'tomleo.urls'

WSGI_APPLICATION = 'tomleo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

db_settings = conf_settings['databases']
DATABASES = {
    'default': {
        'ENGINE': db_settings['default']['type'],
        'NAME': os.path.join(BASE_DIR, db_settings['default']['name']),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
