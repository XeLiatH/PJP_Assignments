'''
Created on 31.10.2012

@author: Jiri Vrany
'''

import reseni
import timeit
import cProfile


POINTS = ((1, 1), (3, 1), (2, 2), (2, 3))


def zmer_basic():
    return reseni.get_triangle(*POINTS)


def measure_time(stat, setup):
    tim_ = timeit.Timer(stat, setup=setup)
    return tim_.timeit(500000)


def main():
    '''
    main routine
    '''
    test_names = ('_basic',)
    for test_name in test_names:
        sta_name = 'zmer{}()'.format(test_name)
        setup_name = "from __main__ import zmer{}".format(test_name)
        print("test name ", sta_name)
        print("10000 opakování trvalo ", measure_time(sta_name, setup=setup_name))
        cProfile.run(sta_name)

if __name__ == '__main__':
    main()
