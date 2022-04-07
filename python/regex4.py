import re

pattern = r'\((\+\d\d\d)\)(\d\d\d-\d\d\d\-\d\d\d)'

myregex = re.compile(pattern)

message = "my number is (+351)123-456-789"

match = myregex.search(message)

print(match.group(1))

print(match.group(2))