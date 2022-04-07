import re

message = "my number is (+351)123-456-789 and my office number is +(+351)999-888-777"

myregex = re.compile(r'\(\+\d\d\d\)\d\d\d-\d\d\d-\d\d\d')

match = myregex.findall(message)

print(match)

