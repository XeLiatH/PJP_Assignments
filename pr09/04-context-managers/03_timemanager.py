import time
import requests

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

def ukazka():
    
    with Timer() as t:
        res = requests.get('http://vrany.nti.tul.cz/')
        print(res.status_code)
        print(res.headers)
    
    print('Request took {:f} sec.'.format(t.interval))


if __name__ == '__main__':
    ukazka()