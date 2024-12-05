import re

s = "The rain in Spain stays mainly in the plain."

match = re.match(r"The", s)

search = re.search(r"Spain", s)

findall = re.findall(r"\bin\b", s)

substitute = re.sub(r"Spain", "France", s)

split = re.split(r"\s", s)

print(match)
print(search)
print(findall)
print(substitute)
print(split)
