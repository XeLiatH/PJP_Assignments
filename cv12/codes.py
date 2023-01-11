# -*- coding: utf-8 -*-

"""

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""

import math
import os.path
import itertools


def generate_primes(boundary, fname):
    """
    Generates prime number up to boundary parameter and stores them in the given file
    """
    if boundary < 0:
        raise ValueError("Given boundary must be a positive value")

    primes = []
    for number in range(2, boundary + 1):
        if all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)):
            primes.append(number)

    with open(fname, 'w') as file:
        for prime in primes:
            file.write(str(prime) + "\n")


def load_primes(prime_length, fname):
    """
    Loads primes from a file by a given length
    """
    if prime_length < 0:
        raise ValueError("Given prime_length must be a positive value")

    if not os.path.isfile(fname):
        boundary = ''
        for _ in range(0, prime_length):
            boundary += str(9)
        generate_primes(int(boundary), fname)

    primes = []
    with open(fname, 'r') as file:
        for line in file:
            clean = line.rstrip()
            if clean.__len__() == prime_length:
                primes.append(int(clean))
            if clean.__len__() > prime_length:
                break

    if not primes:
        os.remove(fname)
        primes = load_primes(prime_length, fname)

    return primes


def find_secret_numbers(prime_length, mask_length, fname):
    """
    Returns the super secret numbers
    """
    primes = load_primes(prime_length, fname)
    mask_rule = [True] * mask_length + [False] * (prime_length - mask_length)
    all_masks = set(list(itertools.permutations(mask_rule, prime_length)))

    codes = []
    for mask in all_masks:
        for prime in primes:
            y_digits = []
            base = []
            for i, digit in enumerate(str(prime)):
                if mask[i]:
                    y_digits.append(digit)
                    base.append('#')
                else:
                    base.append(digit)
            if len(set(y_digits)) == 1:
                codes.append((prime, ''.join(base)))

    codes = sorted(codes, key=lambda x: x[1])
    for mask, code_group in itertools.groupby(codes, lambda x: x[1]):
        tmp = list(code_group)
        if len(tmp) > prime_length + 1:
            for prime in tmp:
                yield prime[0]


if __name__ == '__main__':
    CODES = find_secret_numbers(6, 3, 'primes.txt')
    with open('new_codes.txt', 'w') as file:
        for code in CODES:
            file.write(str(code) + "\n")
