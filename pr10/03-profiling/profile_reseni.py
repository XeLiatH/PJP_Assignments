'''
Created on 31.10.2012

@author: Jiri Vrany
'''

import reseni
import reseni_ref
import reseni_gen
import reseni_sqrt
import timeit
import cProfile


POINTS = ((1, 1), (3, 1), (2, 2), (2, 3))


def zmer_basic():
    return reseni.get_triangle(*POINTS)


def zmer_ref():
    return reseni_ref.get_triangle(*POINTS)


def zmer_gen():
    return reseni_gen.get_triangle(*POINTS)


def zmer_sqrt():
    return reseni_sqrt.get_triangle(*POINTS)


def measure_time(stat, setup):
    tim_ = timeit.Timer(stat, setup=setup)
    return tim_.timeit(1000000)


def main():
    '''
    main routine
    '''
    test_names = ('_basic', '_ref', '_gen', '_sqrt')
    for test_name in test_names:
        sta_name = 'zmer{}()'.format(test_name)
        setup_name = "from __main__ import zmer{}".format(test_name)
        print("test name ", sta_name)
        print("1000000 opakování trvalo ", measure_time(sta_name, setup=setup_name))
        cProfile.run(sta_name)

if __name__ == '__main__':
    main()
