import os
from pathlib import Path
from decouple import config, Csv


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# for PythonAnywhere
ALLOWED_HOSTS.append('yourusername.pythonanywhere.com')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'travels',
    'bookings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travel_booking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'travel_booking.wsgi.application'

# Database: SQLite by default; switch to MySQL by setting DB_ENGINE=mysql
db_engine = os.environ.get("DB_ENGINE", "mysql")
if db_engine == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DATABASE', 'Travel'),
            'USER': os.environ.get('MYSQL_USER', 'root'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'root'),
            'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
            'PORT': os.environ.get('MYSQL_PORT', '3306'),
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'travel_list' 
LOGOUT_REDIRECT_URL = 'login'

# Session settings
SESSION_ENGINE = "django.contrib.sessions.backends.db"  
SESSION_COOKIE_AGE = 1209600  
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  
SESSION_SAVE_EVERY_REQUEST = True 

