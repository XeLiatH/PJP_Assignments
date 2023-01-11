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
    """
    Tato implementace si instanci api vytváří sama 
    což je sice chyba, ale setkáte se s tím docela často
    Jak to otestovat?
    """

    def __init__(self, basic_url):
        self.base = basic_url
        self.web_api = WebApi()

    def refresh_data(self):
        result = self.web_api.get(self.base)
        if result['status'] == 200:
            return True
        else:
            return False    



