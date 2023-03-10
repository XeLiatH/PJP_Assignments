#!/usr/bin/env python
from multiprocessing import Lock, Process, Queue, current_process
import time

import common

def worker(work_queue, done_queue):
    """
    Worker si bere data z fronty, dokud tam nějaká jsou a volá na ně procesní funkci
    """
    try:
        for url in iter(work_queue.get, 'STOP'):
            url_title = common.get_title(url)
            done_queue.put("{} got {}.".format(current_process().name, url_title))

    except Exception as e:
        done_queue.put("{} failed on {} with: {}".format(current_process().name, url, e))
    return True


def main():
    """
    příklad používá dvě fronty 
    frontu url ke zpracování : work_queue
    frontu výsledků: done_queue
    """
    work_queue = Queue()
    done_queue = Queue()
    processes = []

    start = time.time()

    for url in common.SITES:
        work_queue.put(url)

    for w in range(common.JOBS):
        # nastartujeme nový process - worker musí dostat frontu jako argument
        p = Process(target=worker, args=(work_queue, done_queue))
        p.start()
        processes.append(p)
        # STOP příkaz musíme přidat pro každý process který jsme vytvořili
        work_queue.put('STOP')

    # synchronizace výsledků    
    for p in processes:
        p.join()

    done_queue.put('STOP')

    ex_time = time.time() - start


    # tisk výsledků z fronty
    for status in iter(done_queue.get, 'STOP'):
        print(status)

    # jak dlouho to trvalo
    print("Execution time = {0:.5f}".format(ex_time))        
    

if __name__ == '__main__':
    main()