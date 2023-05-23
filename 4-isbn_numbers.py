import re

isbns = ['ISBN 978-3-126-14810-0',
             'ISBN',
             'ISBN 276-3-006-12310-5',
             ]


regex = '^ISBN\s\d{3}-\d{1}-\d{3}-\d{5}-\d{1}$'

for isbn in isbns:
    match = re.search(regex, isbn)
    if match:
        print(isbn)