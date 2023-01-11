"""
Dvě jednoduché třídy pro ukázku mock objektů
"""

import json


class WebApi:

    def __init__(self):
        pass

    def get(self, endpoint):
        """
        @param string url of endpoint
        @return string json
        """
        pass

    def post(self, endpoint):
        pass



class App:
    """
    aplikace používá API a základní URL 
    oba objekty dostává při inicializaci - to vyrazně usnadňuje testování 
    
    aplikace se nemusí starat o to, jak a kdy bude vytvořená instance web_api 
    to je úkol pro jinou komponentu - napřiklad DI kontejner
    """
    def __init__(self, basic_url, web_api):
        self.base = basic_url
        self.web_api = web_api

    def refresh_data(self):
        self.web_api.get(self.base)



