with open('input12.txt') as f:
    inputs = f.readlines()


dirs= ['N', 'E', 'S', 'W']
x_pos = 0
y_pos = 0

dir = 1

for line in inputs:
    instruction = line[0]
    dist = int(line[1:])
    if instruction == 'R':
        dir += int(dist/90)
        dir = dir % 4
        continue
    elif instruction == 'L':
        dir -= int(dist/90)
        dir = dir % 4
        continue
    elif instruction == 'F':
        instruction = dirs[dir]

    if instruction == 'N':
        y_pos += dist
    elif instruction == 'S':
        y_pos -= dist
    elif instruction == 'E':
        x_pos += dist
    elif instruction == 'W':
        x_pos -= dist

print(abs(x_pos) + abs(y_pos))