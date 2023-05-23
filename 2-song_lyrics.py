import re

lyrics = ['[Verse 1] beat it boy',
          '[Verse 500] any verse',
          '[Verse X] everything is alright',
          ]

regex = '^\[Verse \d+\] (.+)'

for lyric in lyrics:
    match = re.search(regex, lyric)
    if match:
        print(lyric)
