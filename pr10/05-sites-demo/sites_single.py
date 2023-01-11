#!/usr/bin/env python

import time


import common

def main():
    
    
    start = time.time()

    for url in common.SITES:
        title = common.handle_url(url)
        if title:
            print("current title for {} is {}".format(url, title))
        else:
            print("site {} is not available - delete it from queue".format(url))

    print("Execution time = {0:.5f}".format(time.time() - start))    


if __name__ == '__main__':
    main()