import sys


def sqrt(x):
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess

# Do early check


def sqrt_1(x):
    if x < 0:
        raise ValueError("Cannot compute square of " f"negative number {x}")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt_1(9))
        print(sqrt_1(16))
        print(sqrt_1(-1))
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
