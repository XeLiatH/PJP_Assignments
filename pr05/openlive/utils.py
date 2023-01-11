"""
common utils for both examples
"""
import urllib.request


def get_data_from_url(url):
    """
    return data from the url
    """
    with urllib.request.urlopen(url) as f:
        html_doc = str(f.read())
    
    return html_doc