import glob
import os
from pprint import pprint as pp
country_to_capital = {
    'United Kingdom': 'London',
    'Brazil': 'Brasilia',
    'Morocco': 'Robot',
    'Sweden': 'Stockholm'
}


capital_to_country = {capital: country for country,
                      capital in country_to_capital.items()}

print(f'Capital to country::{capital_to_country}')

pp(capital_to_country)

words = ['hi', 'hello', 'foxtrot', 'hotel']

word_details = {x[0]: x for x in words}

print(word_details)


file_sizes = {os.path.realpath(p): os.stat(
    p).st_size for p in glob.glob('*.py')}

pp(file_sizes)
