string = '12345612346'
count = {}

for i in string:
    count.setdefault(i,0)
    count[i] += 1
    
print(count)