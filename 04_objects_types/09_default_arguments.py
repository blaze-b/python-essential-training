def banner(message, border='-'):
    print('message = ', message, ", border = ", border)
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Test")

banner("Hello", "*")

banner("Hello World", "*")

banner("Sun, Moon and Stars", border="*")

# Freedom to apply in any order

banner(border="*", message="Hello from earth")