with open('input7.txt') as f:
    inputs = f.readlines()

contains = {}
contained_by = {}

for line in inputs:
    line = line.replace('bags', '')
    line = line.replace('bag', '')
    outside, inside = line.split('contain')
    outside = outside.strip()
    contains[outside] = set()
    inners = inside.split(',')
    for bag in inners:
        if 'no other' in bag:
            continue
        rule = bag.strip(' .\n')
        count, color = rule.split(' ', 1)
        contains[outside].add((color, int(count)))
        if color in contained_by.keys():
            contained_by[color].add(outside)
        else:
            contained_by[color] = {outside,}

inners = {'shiny gold',}
outers = set()
processed = set()

while inners:
    for bag in inners:
        if bag in contained_by.keys():
            outers = outers | contained_by[bag]
        processed.add(bag)
    inners = outers - processed
print(len(outers))


def count_insides(color):
    count = 0
    if color not in contains.keys():
        return count
    for inner in contains[color]:
        count += inner[1] * (count_insides(inner[0]) + 1)
    return(count)


print(count_insides('shiny gold'))
