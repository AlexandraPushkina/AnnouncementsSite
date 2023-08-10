"""
Django settings for announcements project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os  #os.path.join()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  #путь к папке


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-63pwwe8p%^vnage)$j&vca%rd+6z$7_yiq0az*$q+j39ll6t2-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True   #отладочный или экспуатационный сайт

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',   #административный сайт
    'django.contrib.auth',   #подстистема разграничения доступа
    'django.contrib.contenttypes',  #список всех моделей
    'django.contrib.sessions',   #обрабатывает серверные сессии
    'django.contrib.messages',  #всплывающие сообщения
    'django.contrib.staticfiles',  #статические файлы
    'bboard.apps.BboardConfig',
    'main.apps.MainConfig',  #добавляем пакет main
    'bootstrap4',   #программное ядро библиотеки bootstrap4
]

MIDDLEWARE = [    #посредник(обрабатывает ответ между клиентом и сервером)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',   #предварительная обработка запросов
    'django.middleware.csrf.CsrfViewMiddleware',   #защита от межсайтовых атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #посредник разграничения доступа
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  #защита от сетевых атак
]

ROOT_URLCONF = 'announcements.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'announcements.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   #можно заменить на другие бд
        'NAME': os.path.join(BASE_DIR, 'bboard.data'),   #в папке хранится бд
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'  #язык системных сообщений

TIME_ZONE = 'UTC'

USE_I18N = True   #перевод системных сообщений

USE_TZ = True  #дата хранения значений


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'