import multiprocessing
import random
import time
import demotools

def single(data):
    """
    rozklad čísla na prvočísla na jednom jádře
    """
    cisla = list(map(demotools.rozklad, data))


def multi(data, cores):
    """
    paralelní zpracování na dostupných jádrech
    """
    mpool = multiprocessing.Pool(cores)
    cisla = mpool.map(demotools.rozklad, data)


def main():
    """
    Rozklad 100 000 náhodných čísel od 100 do 1 000 000 na prvočísla
    """
    data =[random.randint(100, 1000000) for x in range(100000)] 

    t = time.time()
    single(data)
    single_time = time.time() - t
    print("single core runtime {}".format(single_time))

    cores = multiprocessing.cpu_count()
    print("dostupno {} jader".format(cores))

    for core in range(1, cores+1): 
        t = time.time()
        multi(data, core)
        multi_time = time.time() - t
        print("{} cores runtime {}".format(core, multi_time))
        print("scale factor {:2f} ".format(single_time/multi_time))    

    
    
    
    



if __name__ == "__main__":
    main()
