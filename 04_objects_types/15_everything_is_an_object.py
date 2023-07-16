import samples.word


class_obj = samples.word

typo = type(class_obj)

print(typo)

# to reveal its attributes
dir = dir(class_obj)

print(dir)

typo = type(class_obj.fetch_words)

print(typo)

# print(dir(class_obj.fetch_words))

print(class_obj.fetch_words.__doc__)


print(class_obj.fetch_words.__name__)



