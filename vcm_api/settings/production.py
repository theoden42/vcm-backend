from .base import *  # noqa: F403, F401
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f7f4a1b (populate ALLOWED_HOSTS and CORS_ORIGIN_WHITELIST using environment variable in production)
import os

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '').split(',')
<<<<<<< HEAD
=======
>>>>>>> 7eeb7f5 (modularise settings for production and development)
=======
>>>>>>> f7f4a1b (populate ALLOWED_HOSTS and CORS_ORIGIN_WHITELIST using environment variable in production)
