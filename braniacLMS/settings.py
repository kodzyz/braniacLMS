"""
Django settings for braniacLMS project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nf%v&y$x65co32oy&u9zg4o2f^$6gc(dbyl)(7a2fx)0ro+e5&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # состояние отладки

ALLOWED_HOSTS = []  # список хостов, адреса для защиты от кросформенных запросов

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',

    'social_django',

    'mainapp',
    'authapp',
]  # установленные приложения

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]  #

ROOT_URLCONF = 'braniacLMS.urls'  # точка входа

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # пакет для обработки шаблонов
        'DIRS': ['templates'],  # где ещё могут быть шаблоны для проэкта
        'APP_DIRS': True,  # внутри каждого приложения может быть папка с шаблонами templates
        'OPTIONS': {
            'context_processors': [  # расширение контекста
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainapp.context_processor.my_context_processor',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'braniacLMS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
]  # классы описывающие каким должен быть пароль

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'authapp.User'
LOGIN_REDIRECT_URL = 'mainapp:index'  # url при входе или выходе
LOGOUT_REDIRECT_URL = 'mainapp:index'
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = 'cdd41f9830bed7587936'
SOCIAL_AUTH_GITHUB_SECRET = 'b97beb832b9ce4643072b1cddee504901d33c401'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOG_FILE = BASE_DIR / "log" / "main_log.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[%(asctime)s] %(levelname)s %(name)s (%(lineno)d)%(message)s"},
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "console",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
    },
    "loggers": {
        "django": {"level": "INFO", "handlers": ["file", "console"]},
    },
}
