import re

example = "Welcome to the world of Python"

pattern = r'Python'

match = re.search(pattern, example)

if match:
    print("found", match.group())
else:
    print("No match found.")


