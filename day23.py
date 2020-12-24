import time

input = [int(num) for num in '123487596']


def one_round(cups):
    current_cup = cups[0]
    next_three = cups[1:4]
    cups = cups[4:] + [current_cup]
    next_cup = (current_cup - 1) % 9
    if next_cup == 0:
        next_cup = 9
    while next_cup in next_three:
        next_cup = (next_cup - 1) % 9
        if next_cup == 0:
            next_cup = 9
    insertion = cups.index(next_cup)
    cups = cups[:insertion + 1] + next_three + cups[insertion + 1:]
    return cups


for i in range(100):
    input = one_round(input)

start = input.index(1)
result = input[start + 1:] + input[:start]
print(result)
