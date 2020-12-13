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


def egcd(a, b):  # copied from stackoverflow post on modular inverse
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):  # copied from stackoverflow post on modular inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def modinv(a, m):  # brute force algorithm - fast enough for this puzzle, and I wrote it myself
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1


lcm = bus_ids[0] * products[bus_ids[0]]
result = 0
for modulus, remainder in chinese_remainder_inputs:
    m = modinv(products[modulus], modulus)
    result += (remainder * products[modulus] * m) % lcm
    result = result % lcm

print(result)