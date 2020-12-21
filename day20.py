with open('input20.txt') as f:
    inputs = f.read()


def strip_edges(tile):
    top = tile[0]
    bottom = tile[-1]
    right = ''.join([row[0] for row in tile])
    left = ''.join([row[-1] for row in tile])
    top = min(int(top, 2), int(top[::-1], 2))
    bottom = min(int(bottom, 2), int(bottom[::-1], 2))
    right = min(int(right, 2), int(right[::-1], 2))
    left = min(int(left, 2), int(left[::-1], 2))
    return top, bottom, right, left


edge_lookup = {}
id_lookup = {}
for block in inputs.split('\n\n'):
    if block.strip() == '':
        print('skipping a block')
        continue
    block = block.replace('.', '0')
    block = block.replace('#', '1')
    lines = block.split('\n')
    label = int(lines[0][5:-1])
    edges = strip_edges(lines[1:])
    for edge in edges:
        if edge in id_lookup.keys():
            id_lookup[edge].append(label)
        else:
            id_lookup[edge] = [label]
    edge_lookup[label] = edges

outer_tiles = set()
prod = 1
count = 0
for edge, ids in id_lookup.items():
    if len(ids) == 1:
        if ids[0] in outer_tiles:
            prod *= ids[0]
            count += 1
        outer_tiles.add(ids[0])

print(prod, count)