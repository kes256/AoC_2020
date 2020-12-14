import time

start = time.time()
with open('input11.txt') as f:
    inputs = f.readlines()

max_x = len(inputs[0].strip())
max_y = len(inputs)


def symbols_to_num(row):
    row = row.strip()
    cols = []
    for symbol in row:
        if symbol == '.':
            cols.append(-1)
        elif symbol == 'L':
            cols.append(0)
        else:
            print(f'Unexpected symbol: {symbol}!')
    return cols


def sit_down(empty, full):
    changes = set()
    for seat in empty:
        sit = True
        for neighbor in neighbor_cache[seat]:
            if neighbor in full:
                sit = False
        if sit:
            changes.add(seat)
    empty -= changes
    full.update(changes)
    if len(changes) == 0:
        return 1
    else:
        return 0


def stand_up(empty, full, tolerance):
    changes = set()
    for seat in full:
        count = len(full.intersection(neighbor_cache[seat]))
        if count >= tolerance:
            changes.add(seat)
    full -= changes
    empty.update(changes)
    if len(changes) == 0:
        return 1
    else:
        return 0


old = [symbols_to_num(x) for x in inputs]

neighbor_cache = {}
empty_seats = set()
full_seats = set()
for x in range(max_x):
    for y in range(max_y):
        if old[y][x] == -1:
            continue
        empty_seats.add((y, x))
        neighbor_set = set()
        for col in range(x - 1, x + 2):
            if not 0 <= col < max_x:
                continue
            for row in range(y - 1, y + 2):
                if not 0 <= row < max_y:
                    continue
                if col == x and row == y:
                    continue
                if old[row][col] != -1:
                    neighbor_set.add((row, col))

        neighbor_cache[(y, x)] = neighbor_set
finished = 0
while finished != 2:
    finished = sit_down(empty_seats, full_seats)
    finished += stand_up(empty_seats, full_seats, 4)

print(len(full_seats), time.time() - start)


start = time.time()
neighbor_cache = {}
empty_seats = set()
full_seats = set()
for x in range(max_x):
    for y in range(max_y):
        if old[y][x] == -1:
            continue
        empty_seats.add((y, x))
        neighbor_set = set()
        for dx in range(-1, 2):
            if not 0 <= x + dx < max_x:
                continue
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                col = x + dx
                row = y + dy
                if not 0 <= row < max_y:
                    continue
                while old[row][col] == -1:
                    if not 0 <= row + dy < max_y:
                        break
                    if not 0 <= col + dx < max_x:
                        break
                    col += dx
                    row += dy

                if old[row][col] != -1:
                    neighbor_set.add((row, col))
        neighbor_cache[(y, x)] = neighbor_set

finished = 0
while finished != 2:
    finished = sit_down(empty_seats, full_seats)
    finished += stand_up(empty_seats, full_seats, 5)


print(len(full_seats), time.time() - start)
