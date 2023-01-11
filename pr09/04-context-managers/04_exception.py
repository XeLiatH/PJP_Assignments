from contextlib import contextmanager

@contextmanager
def safe_list(mlist):
    try:
        yield mlist
    except ValueError as e:
        print("ERROR: ", e)
        
    
    
values = [10, 20]    
with safe_list(values) as data:
    for pokus in range(10, 50, 10):
        print(data.index(pokus))
    