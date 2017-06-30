import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd8068ci2cgjmgq',
		'USER': 'rjcjryichndfex',
		'PASSWORD': 'ukkcq_DRmIgSV5-ZZd4Te0VqHF',
		'HOST': 'ec2-54-243-249-132.compute-1.amazonaws.com',
		'PORT': '5432',
    }