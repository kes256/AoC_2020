import re

with open('input20.txt') as f:
    inputs = f.read()


def strip_edges(tile):
    top = tile[0]
    bottom = tile[-1]
    right = ''.join([row[-1] for row in tile])
    left = ''.join([row[0] for row in tile])
    top = min(int(top, 2), int(top[::-1], 2))
    bottom = min(int(bottom, 2), int(bottom[::-1], 2))
    right = min(int(right, 2), int(right[::-1], 2))
    left = min(int(left, 2), int(left[::-1], 2))
    return top, right, bottom, left


edge_lookup = {}
id_lookup = {}
tile_lookup = {}
for block in inputs.split('\n\n'):
    if block.strip() == '':
        print('skipping a block')
        continue
    tile = block.replace('.', '0')
    tile = tile.replace('#', '1')
    lines = tile.split('\n')
    label = int(lines[0][5:-1])
    tile_lookup[label] = lines[1:]
    edges = strip_edges(lines[1:])
    for edge in edges:
        if edge in id_lookup.keys():
            id_lookup[edge].append(label)
        else:
            id_lookup[edge] = [label]
    edge_lookup[label] = edges

outer_tiles = set()
outer_edges = set()
prod = 1
count = 0
corner_id = 0
for edge, ids in id_lookup.items():
    if len(ids) == 1:
        outer_edges.add(edge)
        if ids[0] in outer_tiles:
            prod *= ids[0]
            count += 1
            corner_id = ids[0]
        outer_tiles.add(ids[0])

print(prod, count)

print(len(max(id_lookup.values(), key=lambda x: len(x))))


def join_tile(grid, x, y):
    if x > 0 and y > 0:
        left = grid[x - 1][y]['right']
        old_id = grid[x - 1][y]['id']
        top = grid[x][y - 1]['bottom']
        tile = [i for i in id_lookup[left] if i != old_id][0]
        tile_edges = edge_lookup[tile]
    elif x > 0:
        left = grid[x - 1][y]['right']
        old_id = grid[x - 1][y]['id']
        tile = [i for i in id_lookup[left] if i != old_id][0]
        tile_edges = edge_lookup[tile]
        left_location = tile_edges.index(left)
        if tile_edges[left_location - 1] in outer_edges:
            top = tile_edges[left_location - 1]
        else:
            top = tile_edges[left_location - 3]
    else:
        top = grid[x][y - 1]['bottom']
        old_id = grid[x][y - 1]['id']
        tile = [i for i in id_lookup[top] if i != old_id][0]
        tile_edges = edge_lookup[tile]
        top_location = tile_edges.index(top)
        if tile_edges[top_location - 1] in outer_edges:
            left = tile_edges[top_location - 1]
        else:
            left = tile_edges[(top_location + 1) % 4]
    top_location = tile_edges.index(top)
    flip = (left != tile_edges[top_location - 1])
    bottom = tile_edges[top_location - 2]
    if not flip:
        right = tile_edges[(top_location + 1) % 4]
    else:
        right = tile_edges[top_location - 1]
    grid[x][y]['bottom'] = bottom
    grid[x][y]['right'] = right
    grid[x][y]['rotation'] = top_location
    grid[x][y]['flip'] = flip
    grid[x][y]['id'] = tile
    return bottom in outer_edges, right in outer_edges


x = 0
y = 1
rotation = 0
starting_edges = []
indices = []
for index, edge in enumerate(edge_lookup[corner_id]):
    if edge not in outer_edges:
        starting_edges.append(edge)
        indices.append(index)
        rotation = index - 1 % 4
flip = (indices[0] - 1) % 4 != (indices[1] % 4)
if flip:
    rotation = (rotation + 2) % 4
grid = [[{'id': corner_id,
          'bottom': starting_edges[0],
          'right': starting_edges[1],
          'flip': flip,
          'rotation': rotation}]]
complete = False
max_y = 0
while not complete:
    grid[x].append({})
    bottom, right = join_tile(grid, x, y)
    y += 1
    if bottom:
        max_y = y
        y = 0
        x += 1
        grid.append([])
    complete = bottom and right

max_x = x


def orient_tile(block, rotation, flip):
    if flip:
        return orient_tile([line[::-1] for line in block], (4 - rotation) % 4, False)
    elif rotation == 0:
        return block
    else:
        length = len(block)
        block = [''.join([line[i] for line in block]) for i in range(length - 1, -1, -1)]
        return orient_tile(block, (rotation - 1) % 4, flip)


for column in grid:
    for block in column:
        block_id = block['id']
        rotation = block['rotation']
        flip = block['flip']
        tile_lookup[block_id] = orient_tile(tile_lookup[block_id], rotation, flip)

image = []

for y in range(max_y):
    blocks = [tile_lookup[grid[x][y]['id']][1:-1] for x in range(max_x)]
    for i in range(len(blocks[0])):
        line = ''.join([block[i][1:-1] for block in blocks])
        image.append(line)

sea_monster = ['                  # '.replace(' ', '.').replace('#', '1'),
               '#    ##    ##    ###'.replace(' ', '.').replace('#', '1'),
               ' #  #  #  #  #  #   '.replace(' ', '.').replace('#', '1')]

sea_regex = [re.compile(pattern) for pattern in sea_monster]


def scan_image(test_image, sea_regex):
    monsters = 0
    line_matches = []
    for line in test_image:
        indices = {0: [], 1: [], 2: []}
        for part in range(3):
            match = sea_regex[part].search(line)
            while match:
                start = match.start()
                indices[part].append(start)
                match = sea_regex[part].search(line, start + 1)
        line_matches.append(indices)

    for i in range(len(line_matches) - 2):
        head = line_matches[i]
        middle = line_matches[i + 1]
        bottom = line_matches[i + 2]
        count = set(head[0]).intersection(middle[1]).intersection(bottom[2])
        monsters += len(count)


    if monsters > 0:
        print(f'found {monsters} monsters!')
    return monsters

max_monsters = 0
for rotation in range(4):
    test_image = orient_tile(image, rotation, True)
    count = scan_image(test_image, sea_regex)
    if count > max_monsters:
        max_monsters = count
    test_image = orient_tile(image, rotation, False)
    count = scan_image(test_image, sea_regex)
    if count > max_monsters:
        max_monsters = count

sea_monster_characters = 15

roughness = 0
for line in image:
    roughness += line.count('1')
print(roughness - sea_monster_characters * max_monsters)