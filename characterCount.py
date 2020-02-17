string = '12345612346'
repeats = {}

for i in string:
    repeats.setdefault(i,0)
    repeats[i] += 1

for item in repeats.items():
    print(item)
