import time
with open('input24.txt') as f:
    inputs = f.readlines()

tiles = set()
for line in inputs:
    x = 0
    y = 0
    step = 1
    for char in line:
        if char == 'n':
            y += 1
            step = 0.5
        elif char == 's':
            y -= 1
            step = 0.5
        elif char == 'e':
            x += step
            step = 1
        elif char == 'w':
            x -= step
            step = 1
    if (x, y) in tiles:
        tiles.remove((x, y))
    else:
        tiles.add((x, y))

print(len(tiles))

start_time = time.time()
neighbors = {}


def flip_tiles(black_tiles):
    to_black = set()
    white_neighbors = set()
    to_white = set()
    for tile in black_tiles:
        if tile in neighbors.keys():
            adjacent_tiles = neighbors[tile]
        else:
            x, y = tile
            adjacent_tiles = {(x + 1, y), (x - 1, y),
                              (x + 0.5, y + 1), (x - 0.5, y + 1),
                              (x + 0.5, y - 1), (x - 0.5, y - 1)}
            neighbors[tile] = adjacent_tiles
        black_neighbors = adjacent_tiles.intersection(black_tiles)
        white_neighbors.update(adjacent_tiles - black_neighbors)
        if len(black_neighbors) not in [1, 2]:
            to_white.add(tile)

    for tile in white_neighbors:
        if tile in neighbors.keys():
            adjacent_tiles = neighbors[tile]
        else:
            x, y = tile
            adjacent_tiles = {(x + 1, y), (x - 1, y),
                              (x + 0.5, y + 1), (x - 0.5, y + 1),
                              (x + 0.5, y - 1), (x - 0.5, y - 1)}
            neighbors[tile] = adjacent_tiles
        black_neighbors = adjacent_tiles.intersection(black_tiles)
        if len(black_neighbors) == 2:
            to_black.add(tile)

    black_tiles -= to_white
    black_tiles.update(to_black)


for _ in range(100):
    flip_tiles(tiles)

print(len(tiles), time.time() - start_time)
