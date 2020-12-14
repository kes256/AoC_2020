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


def update_address(num, fixed, floating):
    address_list = []
    base_num = (num & ~floating) | fixed
    floating = bin(floating)[2:]
    length = len(floating)
    floating_bits = [floating.find('1'),]
    count = floating.count('1')
    for i in range(count - 1):
        floating_bits.append(floating.find('1', floating_bits[-1]+1))
    for bits in range(2 ** count):
        alteration = floating
        changes = format(bits, f'0{count}b')
        for bit in range(count):
            i = floating_bits[bit]
            if i == 0:
                alteration = changes[bit] + alteration[i + 1:]
            elif i == length - 1:
                alteration = alteration[:i] + changes[bit]
            else:
                alteration = alteration[:i] + changes[bit] + alteration[i + 1:]
        address_list.append(base_num + int(alteration, 2))
    return address_list


registers = {}
fixed = 0
floating = 0
for line in inputs:
    instruction, value = line.split(' = ')
    if instruction == 'mask':
        fixed, floating = read_bitmask(value)
    else:
        location = int(instruction[4:-1])
        for address in update_address(location, fixed, floating):
            registers[address] = int(value)

print(sum(registers.values()))
