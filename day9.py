with open('input9.txt') as f:
    inputs = f.readlines()

ints = [int(x) for x in inputs]


def check_validity(prev, num):
    diffs = [num - x for x in prev if x != num - x]
    valid = False
    for x in diffs:
        if x in prev:
            valid = True
            break
    return valid

length = len(ints)
for index in range(25, length):
    if not check_validity(ints[index-25:index], ints[index]):
        goal = ints[index]
        break

print(goal)

total = ints[0]
start = 0
stop = 1

while 1:
    if total < goal:
        total += ints[stop]
        stop += 1
    elif total > goal:
        total -= ints[start]
        start += 1
    else:
        span = ints[start:stop]
        break

print(min(span) + max(span))