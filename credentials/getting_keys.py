from configparser import ConfigParser

class key_data:
    def __init__(self) -> None:
        pass

    def api_keys(self):

        config=ConfigParser()
        config.read(['config.ini'])
        api_keys=config['api_keys']['api']
        return api_keys
    
    def mongoDB(self):
        pass