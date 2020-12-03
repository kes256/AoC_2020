with open('input3.txt') as f:
    inputs = f.readlines()

mod = len(inputs[0].strip())
count = {1: 0, 3: 0, 5: 0, 7: 0}
count_2 = 0
col = {1: 0, 3: 0, 5: 0, 7: 0}
col_2 = 0
row = 0
for line in inputs:
    line = line.strip()
    for key in count.keys():
        if line[col[key]] == '#':
            count[key] += 1
        col[key] = (col[key] + key) % mod
    if row == 0:
        if line[col_2] == '#':
            count_2 += 1
        col_2 = (col_2 + 2) % mod
        row = 1
    else:
        row = 0

prod = 1
for value in count.values():
    prod *= value
prod *= count_2
print(prod)
