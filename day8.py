with open('input8.txt') as f:
    inputs = f.readlines()

visited = set()
index = 0
accumulator = 0


def process_instruction(inputs, index, accumulator):
    line = inputs[index]
    op, num = line.split()
    if op != 'jmp':
        index += 1
    else:
        index += int(num)
    if op == 'acc':
        accumulator += int(num)
    return index, accumulator


while index not in visited:
    visited.add(index)
    index, accumulator = process_instruction(inputs, index, accumulator)

print(accumulator)
