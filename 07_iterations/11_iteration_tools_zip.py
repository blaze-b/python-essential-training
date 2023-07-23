from math import sqrt
from itertools import chain
sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]

monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

print([x for x in zip(sunday, monday)])

print([f'average= {(sun + mon)/2}' for sun, mon in zip(sunday, monday)])

tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for temps in zip(sunday, monday, tuesday):
    print(
        f'min = {min(temps):4.1f}, max = {max(temps):4.1f}, average = {sum(temps)/len(temps):4.1f}')

tempertures = chain(sunday, monday, tuesday)

all = all(t > 0 for t in tempertures)

print(all)


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for x in (p for p in lucas() if is_prime(p)):
    print(x)
