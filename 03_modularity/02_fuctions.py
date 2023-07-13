def square(x):
    return x*x

d = square(5);

print("square value::", d)


def launch_missiles():
    print("Launching.....")


launch_missiles()


def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")

w = even_or_odd(31)

print(w)

w = even_or_odd(10)

print(w)

print(w is None)

def nth_root(radicand, n):
    return radicand ** (1/n)

w = nth_root(16, 2)

print(w)

w = nth_root(27, 3)

print(w)
