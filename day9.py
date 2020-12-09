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
        print(ints[index])
        break