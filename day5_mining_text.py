import re

text = "El cliente necesita 3 excavadoras y 2 trituradoras."

machines = re.findall(
    r"(\d+)\s+(excavadoras|trituradoras)",
    text
)

print(machines)


machines = [
    ('3', 'excavadoras'),
    ('2', 'trituradoras')
]

result = []

for x in machines:
    x = {
        "数量": int(x[0]),
        "设备": (x[1])
    }

    result.append(x)

print(result)