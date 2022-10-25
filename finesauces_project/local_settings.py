SECRET_KEY = '!$1d4#&f*^uh4zkqtfj1ekjj25ikpmv(94uzw3nb(*3k%n(6p&'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'postgres',
        'PASSWORD': '773519',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
