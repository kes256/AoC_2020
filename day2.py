with open('input2.txt') as f:
    inputs = f.readlines()

count_a = 0
count_b = 0
for line in inputs:
    rule, pw = line.split(':')
    limits, character = rule.split()
    minimum, maximum = limits.split('-')
    minimum = int(minimum)
    maximum = int(maximum)
    char_count = pw.count(character)
    if minimum <= char_count <= maximum:
        count_a += 1
    if (pw[minimum] == character) ^ (pw[maximum] == character):
        count_b += 1

print(count_b)

# note for part b: 0-based indexing in python balances out with leading whitespace from split
