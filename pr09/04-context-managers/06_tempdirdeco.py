
from os import getcwd, chdir
from contextlib import contextmanager

@contextmanager
def tempdir(tmp_dir):
    orig_dir = getcwd()
    chdir(tmp_dir)
    try:
        yield  #konec __enter__ bloku
    finally:    
        chdir(orig_dir) # __exit__ blok
            

if __name__ == '__main__':
    with tempdir('/home/albert/tmp/'):
        with open('show2.txt', 'w') as tempfile:
            tempfile.write('Song was rumored to be about smoking dried banana skins\n')