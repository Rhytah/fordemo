import os

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URL')
    

class DevelopmentConfig(Config):
    DEBUG=True
    ENV = 'development'
    DATABASE_URI = 'books_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE_URI= 'test_db'
    TESTING = True

class ProductionConfig(Config):
    DEBUG=False
    TESTING = False

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}