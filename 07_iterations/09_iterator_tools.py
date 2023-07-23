from itertools import count, islice
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

print(thousand_primes)

print(list(thousand_primes)[-10:])
