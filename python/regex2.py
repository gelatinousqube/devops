import re
message = "my number is (+351)123-456-789"

#creating regex object with the pattern we are looking for
myregex = re.compile((r'\(\+\d\d\d\)\d\d\d-\d\d\d-\d\d\d'))

match = myregex.search(message)

print(match.group())