import time

with open('input25.txt') as f:
    inputs = f.readlines()

modulus = 20201227
base = 7
pk1, pk2 = [int(x) for x in inputs]
start_time = time.time()

big_steps = int(modulus ** 0.5)
new_base = (base ** big_steps) % modulus

power_lookup = {(new_base ** (i + 1)) % modulus: i + 1 for i in range(big_steps + 1)}
print(time.time() - start_time)


def get_secret_key(public_key):
    i = 0
    power = public_key
    keys = power_lookup.keys()
    while power not in keys:
        power = power * base % modulus
        i += 1
    loops = power_lookup[power] * big_steps - i
    return loops


sk1, sk2 = [get_secret_key(pk1), get_secret_key(pk2)]
exp = sk1 * sk2 % (modulus - 1)
print(base ** exp % modulus, time.time() - start_time)
