#regex : Regular Expressions

import re


usernames = ['Finn  Gary',
        'Osaretin',
        'Tega  Ogohro',
        'Megan  Fame',
        'Night',
        'Waiter',
        'Nectar',
        'Wisemann  Lee',
        'Tivere IDORO',
        'Nelly Albert']

# Find people

regex = '^\w+\s+\w+$'

for name in usernames:
    result = re.search(regex, name)

    if result:
        print(name)
