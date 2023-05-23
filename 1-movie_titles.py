import re

movies = ['Different (1971)',
          'Holy Grail (1975)',
          'Brian (1979)',
          'Moly (2000) the nother']

regex = '^(.+) \(\d{4}\)$'

for movie in movies:
    match = re.search(regex, movie)
    if match:
        print(movie)
