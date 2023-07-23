from math import sqrt

million_squares = (x*x for x in range(1, 100001))

print(list(million_squares)[-10:])


print(list(million_squares))

# to recreate a generator expression, you must execute the expression again

print(sum(x*x for x in range(1, 10000)))


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(sum(x for x in range(1001) if is_prime(x)))
