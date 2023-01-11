from os import getcwd, chdir

class tempdir(object):
    
    def __init__(self, tmp_dir):
        self.tmp_dir = tmp_dir
        self.orig_dir = getcwd()
    
    def __enter__(self):
        chdir(self.tmp_dir)
        
    def __exit__(self, exc_type, exc_value, exc_trace):
        chdir(self.orig_dir)
            

if __name__ == '__main__':
    with tempdir('/home/albert/tmp/'):
        with open('show.txt', 'w') as tempfile:
            tempfile.write('mellow yellow\n')
            
    