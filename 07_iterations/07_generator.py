def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b


print([x for x in lucas()])
