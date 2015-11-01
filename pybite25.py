# coding: utf-8

import re

napis = "kod pocztowy: 61-695 Poznań"

# .+ przynajmniej jedno wystąpienie dowolnego znaku
#pattern = r".+\d{2}-\d{3}.+"

pattern = r"(?P<kod>\d{2}-\d{3})"

# zwróci cały napis
#print(re.match(pattern, napis))

match = re.search(pattern, napis)
print(match)
print(match.groups())
print(match.group())
