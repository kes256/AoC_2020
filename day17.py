import time
with open('input17.txt') as f:
    inputs = f.readlines()

board = set()
y = 0
z = 0
for line in inputs:
    x = 0
    y += 1
    for char in line:
        if char == '#':
            board.add((x, y, z))
        x += 1

start_time = time.time()


def next_generation(cells):
    to_die = set()
    dead_neighbors = set()
    to_live = set()
    for cell in cells:
        x, y, z = cell
        adjacent_cells = {(x + 1, y + 1, z + 1), (x - 1, y + 1, z + 1), (x, y + 1, z + 1),
                          (x + 1, y + 1, z), (x - 1, y + 1, z), (x, y + 1, z),
                          (x + 1, y + 1, z - 1), (x - 1, y + 1, z - 1), (x, y + 1, z - 1),

                          (x + 1, y, z + 1), (x - 1, y, z + 1), (x, y, z + 1),
                          (x + 1, y, z), (x - 1, y, z),
                          (x + 1, y, z - 1), (x - 1, y, z - 1), (x, y, z - 1),

                          (x + 1, y - 1, z + 1), (x - 1, y - 1, z + 1), (x, y - 1, z + 1),
                          (x + 1, y - 1, z), (x - 1, y - 1, z), (x, y - 1, z),
                          (x + 1, y - 1, z - 1), (x - 1, y - 1, z - 1), (x, y - 1, z - 1)}
        #neighbors[cell] = adjacent_cells
        live_neighbors = adjacent_cells.intersection(cells)
        dead_neighbors.update(adjacent_cells - live_neighbors)
        if len(live_neighbors) not in [2, 3]:
            to_die.add(cell)

    for cell in dead_neighbors:
        x, y, z = cell
        adjacent_cells = {(x + 1, y + 1, z + 1), (x - 1, y + 1, z + 1), (x, y + 1, z + 1),
                          (x + 1, y + 1, z), (x - 1, y + 1, z), (x, y + 1, z),
                          (x + 1, y + 1, z - 1), (x - 1, y + 1, z - 1), (x, y + 1, z - 1),

                          (x + 1, y, z + 1), (x - 1, y, z + 1), (x, y, z + 1),
                          (x + 1, y, z), (x - 1, y, z),
                          (x + 1, y, z - 1), (x - 1, y, z - 1), (x, y, z - 1),

                          (x + 1, y - 1, z + 1), (x - 1, y - 1, z + 1), (x, y - 1, z + 1),
                          (x + 1, y - 1, z), (x - 1, y - 1, z), (x, y - 1, z),
                          (x + 1, y - 1, z - 1), (x - 1, y - 1, z - 1), (x, y - 1, z - 1)}
        live_neighbors = adjacent_cells.intersection(cells)
        if len(live_neighbors) == 3:
            to_live.add(cell)

    cells -= to_die
    cells.update(to_live)


for _ in range(6):
    next_generation(board)

print(len(board), time.time() - start_time)


board = set()
y = 0
z = 0
w = 0
for line in inputs:
    x = 0
    y += 1
    for char in line:
        if char == '#':
            board.add((x, y, z, w))
        x += 1

start_time = time.time()


def next_generation_4d(cells):
    to_die = set()
    dead_neighbors = set()
    to_live = set()
    for cell in cells:
        x, y, z, w = cell
        adjacent_cells = {(x1, y1, z1, w1)
                          for x1 in range(x - 1, x + 2)
                          for y1 in range(y - 1, y + 2)
                          for z1 in range(z - 1, z + 2)
                          for w1 in range(w - 1, w + 2)}
        adjacent_cells -= {cell}
        live_neighbors = adjacent_cells.intersection(cells)
        dead_neighbors.update(adjacent_cells - live_neighbors)
        if len(live_neighbors) not in [2, 3]:
            to_die.add(cell)

    for cell in dead_neighbors:
        x, y, z, w = cell
        adjacent_cells = {(x1, y1, z1, w1)
                          for x1 in range(x - 1, x + 2)
                          for y1 in range(y - 1, y + 2)
                          for z1 in range(z - 1, z + 2)
                          for w1 in range(w - 1, w + 2)}
        adjacent_cells -= {cell}
        live_neighbors = adjacent_cells.intersection(cells)
        if len(live_neighbors) == 3:
            to_live.add(cell)

    cells -= to_die
    cells.update(to_live)


for _ in range(6):
    next_generation_4d(board)

print(len(board), time.time() - start_time)
