
from bs4 import BeautifulSoup
import futils



def parse_html(text_data):
    soup = BeautifulSoup(text_data, "lxml")
    result = [" ".join(tag.get('class')) for tag in soup.findAll() if tag.get('class')]
    return result    



if __name__ == "__main__":
    small_file = 'aktualne.html'
    large_file = 'diveintopython3.html'
    data = futils.get_text(large_file)
    print(parse_html(data))
    