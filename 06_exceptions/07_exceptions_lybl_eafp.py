import os

p = '00_images\dict.JPG'


def process_file(p):
    print('Processing file in progress')

# LBYL


if os.path.exists(p):
    process_file(p)
else:
    print(f'No such file as {p}')

# EAFP

try:
    process_file(p)
except OSError as e:
    print(f'Error: {e}')
