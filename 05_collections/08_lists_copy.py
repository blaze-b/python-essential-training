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