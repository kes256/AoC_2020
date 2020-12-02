with open('input1.txt') as f:
    inputs = f.readlines()

nums = [int(x) for x in inputs]
diffs = [2020 - x for x in nums]

match = [x for x in nums if x in diffs]

assert(len(match) == 2)

print(match[0]*match[1])