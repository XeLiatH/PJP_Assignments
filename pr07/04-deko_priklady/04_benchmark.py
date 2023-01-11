'''
Ukazka pouziti dekoratoru pro debug a benchmark funkce
'''
import json
import urllib.request
import decorators
import time

def benchmark(func):
    """
    Decorator ktery vypise, jak dlouho funkce bezela.
    """
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("funkce {} běžela {:.4f}s".format(
            func.__name__, time.clock() - t))
        return res
    return wrapper


@benchmark
@decorators.memoize
def get_data(url):
    '''
    nacte data z Apiary
    '''
    with urllib.request.urlopen(url) as web:
        data = web.read()
        enco = web.info().get_content_charset('utf-8')
        return data.decode(enco)


@benchmark
def decode_json(json_data):
    '''
    Decode 'json_data' 
    '''
    coder = json.JSONDecoder()
    data = coder.decode(json_data)
    return data


def server():
    for _ in range(5):
        data = get_data('http://private-b664-pwa.apiary-mock.com/questions')
        #print(data)
        result = decode_json(data)
        #print(json.dumps(result, sort_keys=True, indent=4))
        time.sleep(0.5)


if __name__ == '__main__':
    server()

    