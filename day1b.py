with open('input1.txt') as f:
    inputs = f.readlines()

nums = [int(x) for x in inputs]
sums = [x + y for x in nums for y in nums]
diffs = [2020 - x for x in sums]

match = [x for x in nums if x in diffs]

assert(len(match) == 3)

print(match[0]*match[1]*match[2])