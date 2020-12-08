with open('input8.txt') as f:
    inputs = f.readlines()


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


def run_program(inputs):
    visited = set()
    length= len(inputs)
    index = 0
    accumulator = 0
    while index not in visited and index < length:
        visited.add(index)
        index, accumulator = process_instruction(inputs, index, accumulator)

    return accumulator, length-index


print(run_program(inputs))

for i in range(len(inputs)):
    if 'nop' in inputs[i]:
        old_input = inputs[i]
        inputs[i] = inputs[i].replace('nop','jmp')
    elif 'jmp' in inputs[i]:
        old_input = inputs[i]
        inputs[i] = inputs[i].replace('jmp','nop')
    else:
        continue
    accumulator, gap = run_program(inputs)
    if gap == 0:
        print(accumulator)
        break
    else:
        inputs[i] = old_input




