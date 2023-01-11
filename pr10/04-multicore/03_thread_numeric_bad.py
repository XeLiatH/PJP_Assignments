"""
Ukázka proč se threading nehodí pro CPU consuming operace
https://www.ploggingdev.com/2017/01/multiprocessing-and-multithreading-in-python-3/
"""

import threading
from queue import Queue
import time

list_lock = threading.Lock()

def find_rand(num):
    sum_of_primes = 0

    ix = 2

    while ix <= num:
        if is_prime(ix):
            sum_of_primes += ix
        ix += 1

    return sum_of_primes

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

def async_worker(in_queue, out_queue):
    while True:
        rand_num = in_queue.get()
        out_queue.put(find_rand(rand_num))
        in_queue.task_done()

def compute():

    input_queue = Queue()
    output_queue = Queue()

    rand_list = [1000000, 2000000, 3000000]

    for i in range(1):
        t = threading.Thread(target=async_worker, args=(input_queue, output_queue))
        t.daemon = True
        t.start()

    start = time.time()

    for rand_num in rand_list:
        input_queue.put(rand_num)

    input_queue.join()

    end_time = time.time()


    for item in output_queue.queue:
            print(item)

    print("Execution time = {0:.5f}".format(end_time - start))

if __name__ == '__main__':
    compute()    