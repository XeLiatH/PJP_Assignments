
from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(open('data/cesky.xml'), "lxml")

    titles = [item.title.string for item in soup.find_all('item')]

    [print(title) for title in titles]
