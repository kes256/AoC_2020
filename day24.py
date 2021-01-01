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
            x += 1
            step = 0.5
        elif char == 's':
            x -= 1
            step = 0.5
        elif char == 'e':
            y += step
            step = 1
        elif char == 'w':
            y -= step
            step = 1
    if (x, y) in tiles:
        tiles.remove((x, y))
    else:
        tiles.add((x, y))

print(len(tiles))
