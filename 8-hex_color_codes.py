import re

color_codes = ['#FF0000',
               '#800000',
               'hvjkjhqe',
               '#000000']

regex = '^#\w{6}$'

for color_code in color_codes:

    match = re.match(regex, color_code)

    if match:
        print(color_code)
