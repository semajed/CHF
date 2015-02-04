"""
Django settings for test_dmp1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%s5#wfkcul4=wfu@sz-6m7)y7x0r@^gc06zo%)+7ch_dbwaiy_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'homepage.User'

USE_L10N = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus.controller',
    'homepage',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mako_plus.controller.router.RequestInitMiddleware',
)

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # never set this True on a live site
LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'simple': {
             'format': '%(levelname)s %(message)s'
         },
     },
     'handlers': {
         'console':{
             'level':'DEBUG',
             'class':'logging.StreamHandler',
             'formatter': 'simple'
         },
     },
     'loggers': {
         'django_mako_plus': {
             'handlers': ['console'],
             'level': 'DEBUG',
             'propagate': False,
         },
     },
}

ROOT_URLCONF = 'test_dmp1.urls'

WSGI_APPLICATION = 'test_dmp1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CHFDB',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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

STATICFILES_DIRS = (
     # SECURITY WARNING: this next line must be commented out at deployment
     BASE_DIR,  
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  

###############################################################
 ###   Specific settings for the Django-Mako-Plus app

 # identifies where the Mako template cache will be stored, relative to each app
DMP_TEMPLATES_CACHE_DIR = 'cached_templates'

 # the default app and page to render in Mako when the url is too short
DMP_DEFAULT_PAGE = 'index'  
DMP_DEFAULT_APP = 'homepage'

 # these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
DMP_DEFAULT_TEMPLATE_IMPORTS = [
   'import os, os.path, re',
]

 # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
 # determines whether DMP will send its custom signals during the process
DMP_SIGNALS = True

 # whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
 # rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
DMP_MINIFY_JS_CSS = True

 # see the DMP online tutorial for information about this setting
DMP_TEMPLATES_DIRS = [ 
   # os.path.join(BASE_DIR, 'base_app', 'templates'),
]

 ###  End of settings for the base_app Controller
 ################################################################
