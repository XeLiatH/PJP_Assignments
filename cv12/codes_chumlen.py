# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 12.

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""
import itertools


def write_primes_to_file(upper_bound, filename):
    """
    generates primes up to n into file
    """
    prime = [True for _ in range(upper_bound + 1)]
    pri = 2
    while pri * pri <= upper_bound:
        if prime[pri]:
            for i in range(pri * 2, upper_bound + 1, pri):
                prime[i] = False
        pri += 1

    with open(filename, 'w') as primes:
        for pri in range(2, upper_bound):
            if prime[pri]:
                primes.write(str(pri) + "\n")


def read_primes(lop, los):
    """
    reads primes of specified length and number of same digits
    """
    len_of_prime = lop
    len_of_sames = los
    filtered_primes = []
    with open('primes.txt', 'r') as primes:
        primes_list = primes.readlines()
    for prime in primes_list:
        prime = prime.strip()
        # načte jen primy, které jsou délky 'len_of_prime' a obsahují 'len_of_sames' stejných číslic
        # (ty co se následně budou v kódu měnit) není nutné, jen optimalizace
        if len(prime) == len_of_prime and len(set(prime)) <= len_of_prime - len_of_sames + 1:
            filtered_primes.append(prime)
        if len(prime) > len_of_prime:
            break

    return filtered_primes


def solve(lop, los, output_fn):
    """
    solves the last, most interesting task that I hope I never met
    """
    primes = read_primes(lop, los)
    len_of_mask = los
    len_of_digit = lop
    # vytvoří masky ve tvaru [True, ..., False, ...] všech kombinací
    template = [True] * len_of_mask + [False] * (len_of_digit - len_of_mask)
    masks_list = set(list(itertools.permutations(template, len_of_digit)))
    codes = []
    # pro každý prime, který má na všech pozicích True stejné číslo vytvoří tuple ve tvaru
    # (prime, maska) např. (56993, 56##3)
    for mask in masks_list:
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

    # seskupí tuply, které mají stejnou masku, skupina, která má předepsanou délku je řešení
    codes = sorted(codes, key=lambda x: x[1])
    for mask, code_group in itertools.groupby(codes, lambda x: x[1]):
        tmp = list(code_group)
        if len(tmp) > lop + 1:
            with open(output_fn, 'w') as ncd:
                for prime in tmp:
                    ncd.write(prime[0] + "\n")


if __name__ == '__main__':
    solve(6, 3, "new_codes.txt")
