# app/config/db.py
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

DB_SYSTEM = {
    'default': {  # Base de datos principal (SQLite)
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    },
    'app1_fuss_db': {  # Primera base de datos externa
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('APP1_FUSS_DB_NAME'),
        'USER': config('APP1_FUSS_DB_USER'),
        'PASSWORD': '',
        'HOST': config('APP1_FUSS_DB_HOST'),
        'PORT': '3306',
    },
    'app1_bixi_db': {  # Primera base de datos externa
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('APP1_BIXI_DB_NAME'),
        'USER': config('APP1_BIXI_DB_USER'),
        'PASSWORD': '',
        'HOST': config('APP1_BIXI_DB_HOST'),
        'PORT': '3306',
    },
    'xui_db': {  # Segunda base de datos externa
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('XUI_DB_NAME'),
        'USER': config('XUI_DB_USER'),
        'PASSWORD': '',
        'HOST': config('XUI_DB_HOST'),
        'PORT': '3306',
    },
    'xui_one_db': {  # Tercera base de datos externa
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('XUI_ONE_DB_NAME'),
        'USER': config('XUI_ONE_DB_USER'),
        'PASSWORD': config('XUI_ONE_DB_PASSWORD'),
        'HOST': config('XUI_ONE_DB_HOST'),
        'PORT': '3306',
    },
}