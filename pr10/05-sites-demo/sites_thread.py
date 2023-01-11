import threading
from queue import Queue
import time

import common
    
def worker(url_queue, result_queue):
    while True:
        current_url = url_queue.get()
        result_queue.put(common.get_title(current_url))
        url_queue.task_done()

def main():
    url_queue = Queue()
    result_queue = Queue()

    for i in range(common.JOBS):
        t = threading.Thread(target=worker, args=(url_queue, result_queue))
        t.daemon = True
        t.start()

    start = time.time()

    for current_url in common.SITES:
        url_queue.put(current_url)

    url_queue.join()
    #result_queue.join()
    ex_time = time.time() - start

    for item in result_queue.queue:
        print(item)

    print("Execution time = {0:.5f}".format(ex_time))

if __name__ == '__main__':
    main()