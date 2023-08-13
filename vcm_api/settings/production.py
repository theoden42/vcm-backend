from .base import *  # noqa: F403, F401
<<<<<<< HEAD
import os

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '').split(',')
=======
>>>>>>> 7eeb7f5 (modularise settings for production and development)
