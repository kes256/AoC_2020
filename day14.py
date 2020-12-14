with open('input14.txt') as f:
    inputs = f.readlines()


def read_bitmask(mask):
    fixed = mask.replace('X', '0')
    variable = mask.replace('1', '0').replace('X', '1')
    fixed = int(fixed, 2)
    variable = int(variable, 2)
    return fixed, variable


def update_number(num, fixed, variable):
    return fixed + (num & variable)


registers = {}
fixed = 0
variable = 0
for line in inputs:
    instruction, value = line.split(' = ')
    if instruction == 'mask':
        fixed, variable = read_bitmask(value)
    else:
        location = int(instruction[4:-1])
        registers[location] = update_number(int(value), fixed, variable)

print(sum(registers.values()))
