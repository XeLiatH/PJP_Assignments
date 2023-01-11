"""
Dvě jednoduché třídy pro ukázku mock objektů
"""

class WebApi:

    def __init__(self):
        pass

    def get(self, endpoint):
        """
        @param string url of endpoint
        @return dict encoded json
        """
        pass

    def post(self, endpoint):
        pass



class App:

    def __init__(self, basic_url, web_api):
        self.base = basic_url
        self.web_api = web_api

    def refresh_data(self):
        result = self.web_api.get(self.base)
        if result['status'] == 200:
            return True
        else:
            return False    



