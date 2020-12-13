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


neighbor_cache = {}


def neighbors(x, y, state):
    neighbor_count = 0
    if (x, y) in neighbor_cache:
        for (i, j) in neighbor_cache[(x, y)]:
            neighbor_count += state[j][i]
    else:
        neighbor_list = []
        for col in range(x - 1, x + 2):
            if not 0 <= col < max_x:
                continue
            for row in range(y - 1, y + 2):
                if not 0 <= row < max_y:
                    continue
                if col == x and row == y:
                    continue
                if state[row][col] != -1:
                    neighbor_list.append((col, row))
                    neighbor_count += state[row][col]
        neighbor_cache[(x, y)] = neighbor_list
    return neighbor_count


def sit_down(seats):
    new_seats = []
    for row in seats:
        new_seats.append(row[:])
    for x in range(max_x):
        for y in range(max_y):
            if seats[y][x] != -1:
                count = neighbors(x, y, seats)
                if not count:
                    new_seats[y][x] = 1
    return new_seats


def stand_up(seats, tolerance):
    new_seats = []
    for row in seats:
        new_seats.append(row[:])
    for x in range(max_x):
        for y in range(max_y):
            if seats[y][x] != -1:
                count = neighbors(x, y, seats)
                if count >= tolerance:
                    new_seats[y][x] = 0
    return new_seats


old = [symbols_to_num(x) for x in inputs]
new = sit_down(old)
while new != old:
    old = new
    new = sit_down(old)
    new = stand_up(new, 4)

count = [[x for x in row if x != -1] for row in new]
count = [sum(row) for row in count]
print(sum(count), time.time() - start)
start = time.time()


def neighbors(x, y, state):
    neighbor_count = 0
    if (x, y) in neighbor_cache:
        for (i, j) in neighbor_cache[(x, y)]:
            neighbor_count += state[j][i]
    else:
        neighbor_list = []
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
                while state[row][col] == -1:
                    if not 0 <= row + dy < max_y:
                        break
                    if not 0 <= col + dx < max_x:
                        break
                    col += dx
                    row += dy

                if state[row][col] != -1:
                    neighbor_list.append((col, row))
                    neighbor_count += state[row][col]
        neighbor_cache[(x, y)] = neighbor_list
    return neighbor_count


neighbor_cache = {}
old = [symbols_to_num(x) for x in inputs]
new = sit_down(old)
while new != old:
    old = new
    new = sit_down(old)
    new = stand_up(new, 5)

count = [[x for x in row if x != -1] for row in new]
count = [sum(row) for row in count]
print(sum(count), time.time() - start)
