import re

usernames = ['@sir_Uracyaryamye',
             '@umuyede6t57239629',
             'wakanda@forever',
             '@more_life'
             ]


regex = '^@\w+'

for username in usernames:
    match = re.search(regex, username)
    if match:
        print(username, "Matches the pattern")

    else:
        print(username, "Deosn't match the pattern")
