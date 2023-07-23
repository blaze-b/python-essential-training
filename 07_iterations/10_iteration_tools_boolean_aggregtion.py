from math import sqrt

b = any([False, False, True])


print(b)

b = all([False, True, True])

print(b)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


b = any(is_prime(x) for x in range(1328, 1361))

print(b)

b = all(name == name.title() for name in ['London', 'Paris'])

print(b)
