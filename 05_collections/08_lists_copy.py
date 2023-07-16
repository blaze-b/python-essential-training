# to copy
s = [1, 78, 78, 56, 777]
r = s[:]

# Only the reference are copied
# The techniques perform shallow copies
print(r is s)

print(r == s)

u = s.copy()

print(u is s)

print(u == s)

v = list(s)

print(v is s)

print(v == s)

a = [[1, 2], [3, 4]]

b = a[:]

print(a is b, a == b)

print(a[0], b[0])

print(a[0] is b[0])

a[0] = [8, 9]

print(a[0], b[0])

a[1].append(5)

print(a[1], b[1])

print(a, b)

c = [21, 37]

d = c * 4

print(d)

print([0] * 9)

s = [[-1, 1]] *5

print(s)

s[2].append(7)

print(s)