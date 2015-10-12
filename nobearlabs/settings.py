# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytz
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Include BOOTSTRAP3_FOLDER in path
BOOTSTRAP3_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '..', 'bootstrap3'))
if BOOTSTRAP3_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP3_FOLDER)


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()


AUTH_USER_MODEL = 'users.CustomUser'
SITE_ID = 1
# Datatbase ==============================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'dbHank4Site330',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]
# Local time zone 
TIME_ZONE = 'Asia/Taipei'
LANGUAGE_CODE = 'zh-tw'
DEFAULT_CHARSET = 'utf-8'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
MEDIA_ROOT = SETTINGS_PATH+'/static/media'
UPLOAD_MEDIA_PATH = MEDIA_ROOT+'/upload'

MEDIA_URL = SETTINGS_PATH+'/media/'

STATIC_ROOT = SETTINGS_PATH+'/static/'
STATICFILES_DIRS = [
    '/static/',
    '/zinnia/static',
]

#STATIC_URL = SETTINGS_PATH+'/static/'
STATIC_URL = '/static/'
STATIC_UPLOAD = STATIC_ROOT + '/upload/'

STATICFILES_FINDERS = [
	"django.contrib.staticfiles.finders.FileSystemFinder",
	"django.contrib.staticfiles.finders.AppDirectoriesFinder"
]



# Product app ===================
PRODUCTLIST = SETTINGS_PATH+"/product/productlist"

# RRD app ======================
RRDPATH = SETTINGS_PATH + '/rrd/db'
RRDLIST = [{'name':'test.rrd','step':300,'vertical_label':'Y'}, ]


# Make this unique, and don't share it with anybody.
SECRET_KEY = '8s)l4^2s&&0*31-)+6lethmfy3#r1egh^6y^=b9@g!q63r649_'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#AUTHENTICATION_BACKENDS=('SettingsBackend','django.contrib.auth.backends.ModelBackend',)
AUTHENTICATION_BACKENDS=('django.contrib.auth.backends.ModelBackend',)


ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates','zinnia'),
)
print TEMPLATE_DIRS,"= = = = = = = = = =  ="
# TEMPLATES SETTING FOR BLOG
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS':[os.path.join(SETTINGS_PATH, 'templates'),os.path.join(SETTINGS_PATH, 'templates','zinnia')],
    'OPTIONS': {
      'context_processors': [
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.i18n',
        'django.template.context_processors.request',
        'django.contrib.messages.context_processors.messages',
        'zinnia.context_processors.version',  # Optional
      ]
    }
  }
]

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
  ('zinnia/_short_entry_detail.html', 'Short entry template'),
]

ZINNIA_ENTRY_DETAIL_TEMPLATES = [
  ('zinnia/fullwidth_entry_detail.html', 'Fullwidth template'),
]

# APPs ==================================================
INSTALLED_APPS = (
    # Django framework
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_comments',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'django.contrib.sitemaps', 
    # Other framework
    'rest_framework',	# For Rest 
    'bootstrap3',	# For BootStrap3
    'social_auth',	# For Social Login ex: FB Twitter
    # My Apps
    'demo',
    'main',
    'api',
    'product', 	# Product introduction 
    'machine', 	# Online machine monitor
    'rrd', 	# My RRD tool interface (for Monitor)
    'users',
    'ds',
    # BLOG Framework
    'tagging',
    'mptt',
#    'zinnia',
)


# Logging ===========================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#=============  Django Social Auth =================

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Keys
TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = '499066306920395'
FACEBOOK_API_SECRET          = '23b633d876ea8252afb798d8f994aa56'

#Urls
LOGIN_URL          = '/login'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

# FB Setting
#FACEBOOK_EXTENDED_PERMISSIONS = ['email']
#FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}
#FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}

SOCIAL_AUTH_SANITIZE_REDIRECTS = False
#SOCIAL_AUTH_REDIRECT_IS_HTTPS = True  # HTTPS
SOCIAL_AUTH_URLOPEN_TIMEOUT = 30
# Pipeline setting

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    #'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    )

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer' 


# ================= Settings for django-bootstrap3 ======================
BOOTSTRAP3 = {
    'set_required': True,
    'error_css_class': 'bootstrap3-error',
    'required_css_class': 'bootstrap3-required',
    'javascript_in_head': True,
#    'css_url':'/root/dist/css/bootstrap.min.css',
}



# ============================  Settings for ReSTful framwork =======================
REST_FRAMEWORK = {
    # 使用 session 登入。
#    'DEFAULT_AUTHENTICATION_CLASSES': (  
#        'rest_framework.authentication.SessionAuthentication',  
#    ),  
    # 必須登入才能使用。  
#    'DEFAULT_PERMISSION_CLASSES': (  
#        'rest_framework.permissions.IsAuthenticated',  
#    ),  
}
