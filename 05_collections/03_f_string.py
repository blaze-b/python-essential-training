value = 4*20

str_format = f'The value is {value}'

print(str_format)

import datetime

str_date_format = f'The current time is {datetime.datetime.now().isoformat()}.'

print(str_date_format)


import math

str_math_details = f'Math Constants: pi={math.pi}, e={math.e}'

print(str_math_details)

str_math_details = f'Math Constants: pi={math.pi:.3f}, e={math.e:.3f}'

print(str_math_details)

help(str)