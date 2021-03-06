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

x_pos = 0
y_pos = 0
waypoint_x = 10
waypoint_y = 1

for line in inputs:
    instruction = line[0]
    dist = int(line[1:])
    if instruction in ['R', 'L']:
        if instruction == 'R':
            dist = 360 - dist
        if dist == 90:
            waypoint_x, waypoint_y = (-waypoint_y, waypoint_x)
        elif dist == 180:
            waypoint_x, waypoint_y = (-waypoint_x, -waypoint_y)
        elif dist == 270:
            waypoint_x, waypoint_y = (waypoint_y, -waypoint_x)
    elif instruction == 'F':
        x_pos += dist*waypoint_x
        y_pos += dist*waypoint_y
    elif instruction == 'N':
        waypoint_y += dist
    elif instruction == 'S':
        waypoint_y -= dist
    elif instruction == 'E':
        waypoint_x += dist
    elif instruction == 'W':
        waypoint_x -= dist

print(abs(x_pos) + abs(y_pos))