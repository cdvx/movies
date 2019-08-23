"""Module for configuration"""

class Config:
    """Base Config class"""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development DevelopmentConfig class"""
    DEBUG = True

class TestingConfig(Config):
    """Development DevelopmentConfig class"""
    DEBUG = True
    TESTING = True

# config dict
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
