# ~*~ coding: utf-8 ~*~

"""
Django settings for devel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't9&+m79!3%t)^y4thx-r@1)ke-w7n#*7k03j-se*4qov6upoz%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'localeurl',	    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haupt',
    'bootstrap3',
    'south',
    'orderform',
    
		
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

LOCALEURL_USE_SESSION = True

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'), 
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
)


LANGUAGE_CODE = 'de-De'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'templates/css'),
)

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)



LANGUAGES = (
    ('ru', 'Russian'),
    ('de', 'Deutsch'),
    ('en', 'English'),
)

#MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
#MODELTRANSLATION_TRANSLATION_REGISTRY = 'webvolant.translation'

# включаем систему перевода django
#USE_I18N = True

# указываем, где лежат файлы перевода
#LOCALE_PATHS = (
#    os.path.join(PROJECT_ROOT, 'locale'),
#)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'


# эта переменная будет указывать на папку проекта

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# путь до папки media, в общем случае она пуста в начале

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'  # URL для медии в шаблонах



