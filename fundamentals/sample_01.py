print("This is my first python file")

# Variables
x = 5
y = 6
print("sum = ", (x + y))
z = 5

# Memory address of x and z will be the same and the z will be different
print("memory location of z = ", id(z))
print("memory location of x = ", id(x))
print("memory location of y = ", id(y))

p = 2
q = 3
r = p + q

# Memory address of x z and r will be the same
print("memory location of r = ", id(r))
