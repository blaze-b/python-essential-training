from samples.exception_1 import *

x = convert("one two three four".split())

print(x)

x = convert_1("one two three four".split())

x = convert_1("one two threee four".split())

x = convert_1(123)

x = convert_2(123)

x = convert_2('two nine'.split())

x = convert_2("elephant".split())

x = convert_2(451)

# Using the pass arguement

x = convert_3(451)

# Single return statement

x = convert_4(451)

# Accessing the exception objects using the as keyword

x = convert_5(451)

x = convert_5("elephant".split())
