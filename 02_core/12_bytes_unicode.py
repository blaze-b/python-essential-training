norsk = "Jeg begynte à fortære en sandwich mens jeg kjørte taxi på vei til quiz"
data = norsk.encode('utf8')
print(data)

norwegian = data.decode('utf8')
print(norwegian)

print(norwegian == norsk)