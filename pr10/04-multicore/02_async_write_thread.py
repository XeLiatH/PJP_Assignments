import threading
import time


class AsyncWrite(threading.Thread):
    """
    I/O operace uvolňují GIL, proto můžeme použít Thread bez obav
    """
    
    def __init__(self, text, output_file):
        super(AsyncWrite, self).__init__()
        self.text = text
        self.out = output_file

    def run(self):
        with open(self.out, 'w') as f:
            f.write(self.text + '\n')
            #aby thread trval dele...
            time.sleep(2)

        print("finished background writing")
        

def main():
    message = "output_file ukazka"
    background = AsyncWrite(message, 'demo_out.txt')
    background.start()
    print("jedeme stale dale")
    print("i procesoru je dost ;-) ", 2**2000)

    # synchroinzace vlaken
    background.join()
    print("thread opravdu skoncil"  )

if __name__ == '__main__':
    main()

