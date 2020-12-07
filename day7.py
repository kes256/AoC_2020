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
        color = bag.strip(' .\n0123456789')
        contains[outside].add(color)
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

