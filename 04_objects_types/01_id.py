a = 10
i = id(a)

print(i)

b = 11
i = id(b)

print(i)

a = b
print(id(a))
print(id(b))

print(a is b)