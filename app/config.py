class Config:
    '''
    General configuration parent class
    '''
     HEADLINES_API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    SOURCE_API_URL='https://newsapi.org/v2/sources?apiKey={}'
    SEARCH_SOURCES='https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')






class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True