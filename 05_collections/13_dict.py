urls = {
    'Google': 'http://google.com',
    'Plurasight': 'http://pluralsight.com'
}

print(urls['Plurasight'])


names_and_ages = [('Alices', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]

print(type(names_and_ages))

phonetic = dict(names_and_ages)

print(phonetic)


# Copy

d = dict(goldenRod=0xDAA520, indigo=0xDAA521, seashell=0xDAA527787)

e = d.copy()

print(e)

f = dict(e)

# Updating

g = dict(wheat=0xDAA527789, khaki=0xDAA527788989, crimson=0xDAA527787878)

f.update(g)

print(f)

print(type(g['wheat']))


stocks = {'GOOG': 891, 'APL': 194, 'IBM': 194}

print(stocks)

stocks.update({'GOOG': 894, 'YHOO': 25})

print(stocks)

# Iterating

colors = dict(aquamarice='#8989898',
              burlywood='#898989',
              chartreuse='#ioioiio',
              cornflower='#lklklkl',
              firebrick='#jjkjkjk',
              honeydew='#lklklkl',
              maroon='#B2222')

for key in colors:
    print(f"{key} => {colors[key]}")

for value in colors.values():
    print(value)

for key in colors.keys():
    print(key)

for key, value in colors.items():
    print(key, value)


symbols = dict(usd='$', gbp='Pound', nzd='$')

print(symbols)

# Contains
print('nzd' in symbols)

# Not contains

print('mzd' not in symbols)


z = {'H': 1, 'TC': 2, 'Xe': 3, 'Fy': 137}

del z['Fy']

print(z)

m = dict(
    H=[1, 2, 3],
    He=[3, 4],
    Li=[7, 9, 10],
    Be=[7, 9],
    B=[10, 11],
    C=[11, 12, 13, 14]
)
m['H'] += [4, 5, 25]

print(m['H'])

# Add a new item

m['N'] = [8, 4, 4]

print(m)

m['N'].append(22)

print(m)
