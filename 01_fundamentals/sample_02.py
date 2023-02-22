# Datatypes - Built-in Datatypes, User Defined Datatypes
# Built-in Datatypes - None, Numeric, Sequences, Sets and Mapping
# None
x = None
print(x)
x = 5
print(x)

# Numeric: int, Float, Complex, Bool
# int
a = 50
print("a type= ", type(a))

# Float
b = 50.5
print("b type= ", type(b))

# Complex
c = 50 + 5j
print("c type= ", type(c))

# Bool
d = 12 > 11
print("d type= ", type(d))
print("d value= ", d)
a = 10
b = 11
if a < b:
    print("Hello")
else:
    print("ok")

# Sequences: String, List, Tuple, Range

# String
my_name = 'Brian'
print(my_name)
my_name1 = "Brian"
print(my_name1)

# List
my_list = ["Brian", 5, 6.3]
print(my_list)
# Index element printing
print(my_list[0])

# Tuple
tp = (15, "un-wired", 10, "learning")
print("tuple= ", tp)
print("1st value = ", tp[0])
print("2nd value = ", tp[1])
print("3rd value = ", tp[2])

# Range
# range(start,stop,step)
r = range(1, 10)
print("range = ", list(r))
r = range(1, 10, 2)
print("range =", list(r))

# Sets
s = {10, 5, 7}
print(s)
s = {10, 8, 77, 10, 6, 5}
print(s)
# print(s[0]) set cannot be indexed
lst = [10, 4, 6, 7]
a = set(lst)
print(a)

# Mappings or Dictionaries
d = {10: "un-wired", 11: "learning"}
print(d)
print(d[10])
di = {1: "Brian", 2: "Geeth", 3: "John"}
print(di[3])
