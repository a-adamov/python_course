list_dict = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

set = set()

for dict in list_dict:
    for k,v in dict.items():
        set.add(v)

print(set)