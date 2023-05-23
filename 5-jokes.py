import re

jokes = ['Why did the tree fall down ? Because of the wind',
          '[Verse 5] any verse',
          '[Verse X] everything is alright',
          ]

regex = '\w+\s\w+\s\?\s\w+'

regex = '\w+\s\w+\s\?\s\w+'

for joke in jokes:
    match = re.search(regex, joke)
    if match:
        print(joke)
