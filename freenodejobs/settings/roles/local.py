from os.path import abspath, dirname, join


def base_dir(*xs):
    return join(dirname(dirname(dirname(dirname(abspath(__file__))))), *xs)


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'freenodejobs',
        'ATOMIC_REQUESTS': True,
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

MEDIA_URL = '/storage/'
MEDIA_ROOT = base_dir('storage')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

REDIS_ENABLED = False
