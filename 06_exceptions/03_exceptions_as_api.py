def sqrt(x):
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(16))
        print(sqrt(-1))
        print("This is never printed")
    except ZeroDivisionError:
        print('Cannot compute square root of a negative number.')
    print('Execution computed successfully')


if __name__ == '__main__':
    main()
