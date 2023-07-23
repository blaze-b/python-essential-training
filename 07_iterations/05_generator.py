def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()

print(g)

# print(next(g), next(g), next(g))

g = [iterator for iterator in g]

print(g)

h = gen123()

i = gen123()

print(h is i)

print(h == i)


def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')


gen = gen246()

print(next(gen))

print(next(gen))

print(next(gen))
