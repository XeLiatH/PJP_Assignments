import bs4
import requests

SITES = (
        'www.tul.cz/',
        'tuni.tul.cz/',
        'www.root.cz/',
        'www.lupa.cz/',
        'www.idnes.cz',
        'www.denik.cz',
        'www.lidovky.cz',
        'www.sport.cz',
        'www.novinky.cz',
        'www.ihned.cz',
        'www.irozhlas.cz',
        'news.yahoo.com/',
        'news.google.com/',
        'www.cnn.com',
        'www.nytimes.com',
        'www.foxnews.com',
        'www.nbcnews.com',
        'www.dailymail.co.uk',
        'www.theguardian.com',
        'www.wsj.com',
        'www.abcnews.go.com',
        'news.bbc.co.uk',
        'www.usatoday.com',
        'www.cyclingnews.com',
        'www.cnn.com',
        'www.nytimes.com',
        'www.google.com',
        'www.theguardian.com',
        'www.indiatimes.com',
        'www.yahoo.com',
        'www.shutterstock.com',
        'www.foxnews.com',
        'www.weather.com',
        'www.forbes.com',
        'www.indiatimes.com',
        'www.usatoday.com',
        'www.cnbc.com',
        'www.bloomberg.com',
        'www.wsj.com',
        'www.drudgereport.com',
        'www.reuters.com',
        'www.nbcnews.com',
        'www.wunderground.com',
        'www.cbsnews.com',
        'www.nypost.com',
        'www.indiatimes.com',
        'www.chron.com',
        'www.news.com.au',
        'www.chinadaily.com.cn',
        'www.theatlantic.com',
        'www.thehill.com',
        'www.time.com',
        'www.indianexpress.com',
        'www.abcnews.go.com',
        'www.dw.com',
        'www.thedailybeast.com',
        'www.weather.gov',
        'www.thehindu.com',
        'www.sfgate.com',
        'www.variety.com',
        'www.hollywoodreporter.com',
        'www.nationalgeographic.com',
        'www.yr.no',
        'www.euronews.com',
        'www.smh.com.au',
        'www.yahoo.com'
) 



JOBS = 4

def handle_url(current_url):
    data = get_url(current_url)
    if data:
        return parse_data(data) 
    return False


def get_url(current_url):
    try:
        res = requests.get("http://{}".format(current_url), timeout=5)
        res.raise_for_status()
        return res
    except requests.exceptions.ReadTimeout as ex:
        print(ex)
        return False
    except requests.exceptions.HTTPError as ex:
        print(ex)
        return False

  
def parse_data(data):

    current_page = bs4.BeautifulSoup(data.text,"html.parser")
    try:
        current_title = current_page.select('title')[0].getText()
    except IndexError:
        current_title = "NO TITLE"    

    return current_title

def get_title(url):
    """
    procesní funkce kterou používá worker
    """
    title = handle_url(url)
    if title:
        return "current title for {} is {}".format(url, title)
    else:
        return "site {} is not available - delete it from queue".format(url)

