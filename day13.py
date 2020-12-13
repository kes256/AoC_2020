with open('input13.txt') as f:
    inputs = f.readlines()

# at a glance, all input ids are prime numbers
current_time = int(inputs[0])

bus_ids = [int(x) for x in inputs[1].split(',') if x != 'x']

next_arrival = {}
for id in bus_ids:
    next_arrival[id] = id - (current_time % id)

id, wait = min(next_arrival.items(), key=lambda x: x[1])
print(id*wait)

minute_constraints = zip(inputs[1].split(','), range(len(inputs[1].split(','))))
chinese_remainder_inputs = []
for row in minute_constraints:
    if 'x' != row[0]:
        chinese_remainder_inputs.append((int(row[0]), row[1]))

products = {}
for i, _ in chinese_remainder_inputs:
    prod = 1
    for j, _ in chinese_remainder_inputs:
        if i == j:
            continue
        prod *= j
    products[i] = prod


def inv(a, m):  # brute force algorithm - fast enough for this puzzle
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1


lcm = bus_ids[0] * products[bus_ids[0]]
result = 0
for modulus, remainder in chinese_remainder_inputs:
    m = inv(products[modulus], modulus)
    result += (remainder * products[modulus] * m) % lcm
    result = result % lcm

print(result)