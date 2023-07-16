import math
str = 'qwertyuiopasdfghjklzxcvbnuyuyujhvgvfvfgbhghbghghhjhnjhjhjh'

l = len(str)

print(l)

str = 'New' + 'found' + 'land'

print(str)

str1 = 'New'
str1 += 'Found'
str1 += 'land'

# str.join()
print(str1)

colors = ";".join(["#uiuuiui", "#uuiuiu", "#uiuiuui", "#uiuiuiui"])

print(colors)

print(colors.split(";"))

str1 = "".join(["high", "way", "man"])

print(str1)

# Partitioning
str_partition = "unforgetable".partition('forget')

print(str_partition)

departure, partition, arrival = "London:Edinburgh".partition(":")

print(arrival, departure)

origin, _, destination = "LHR-TVM".partition("-")

print(origin, destination)


# Str formatting

str_format = "The age of {0} is {1}".format("Jim", 32)

print(str_format)

str_format = "The age of {0} is {1}. {0}'s birthday is on {2}.".format(
    'Fred', 24, 'October 31')

print(str_format)

str_format = "Reticulating spine {} of {}.".format(4, 23)

print(str_format)

"Current position {latitude} {longitude}".format(
    latitude="60N", longitude="5E")

print(str_format)

str_format = "Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=[
                                                                           65.2, 23.1, 82.2])

print(str_format)


str_format = "Math constants: pi = {m.pi}, e={m.e}".format(m=math)

print(str_format)

str_format = "Math constants: pi = {m.pi:.3f}, e={m.e:.3f}".format(m=math)

print(str_format)

value = 4 * 20

str_format = 'The value is {value}'.format(value=value)

print(str_format)
