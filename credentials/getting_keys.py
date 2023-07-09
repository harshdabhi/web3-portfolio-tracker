from configparser import ConfigParser

class key_data:
    def __init__(self) -> None:
        pass

    def api_keys(self,api_name):

        config=ConfigParser()
        config.read(['config.ini'])
        api_keys=config['api_keys'][api_name]
        return api_keys
    
    def mongoDB(self):
        pass