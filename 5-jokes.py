import re

jokes = ['Why did the tree fall down ? Because of the wind',
          '[Verse 5] any verse',
          '[Verse X] everything is alright',
          ]

regex = '^(Why did the .+\?)\s(Because .+)'

for joke in jokes:
    match = re.search(regex, joke)
    if match:
        print(joke)
