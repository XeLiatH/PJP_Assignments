# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro program codes.py
"""

import codes
import pytest
import os.path


def test_generate_primes():
    with pytest.raises(ValueError):
        codes.generate_primes(-5, 'test.txt')


def test_generate_primes_file():
    codes.generate_primes(2, 'test.txt')

    assert os.path.isfile('test.txt')


def test_load_primes():
    with pytest.raises(ValueError):
        codes.load_primes(-5, 'test.txt')


def test_load_primes_values():
    os.remove('test.txt')
    arr = [2, 3, 5, 7]
    primes = codes.load_primes(1, 'test.txt')

    assert arr == primes


def test_load_primes_values_wrong():
    os.remove('test.txt')
    arr = [2, 3, 5, 7]
    primes = codes.load_primes(2, 'test.txt')

    assert arr != primes

def test_secret_numbers():
    arr = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
    secret = []
    for code in codes.find_secret_numbers(5, 2, 'test.txt'):
        secret.append(code)

    assert arr == secret
