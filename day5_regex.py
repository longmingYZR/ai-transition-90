import re

text = "El proyecto necesita 3 excavadoras."

numbers = re.findall(r"\d+", text)

print(numbers)
