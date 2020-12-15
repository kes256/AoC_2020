import time

start = time.time()

inputs = [6, 19, 0, 5, 7, 13, 1]

last_seen = {}
for num, index in zip(inputs, range(len(inputs))):
    last_seen[num] = (0, index)

i = len(inputs)
say = inputs[-1]
while i < 2020:
    indices = last_seen[say]
    say = indices[0]
    if say not in last_seen:
        last_seen[say] = (0, i)
    else:
        gap = i - last_seen[say][1]
        last_seen[say] = (gap, i)

    i += 1

print(say, time.time() - start)
start = time.time()

while i < 30000000:
    indices = last_seen[say]
    say = indices[0]
    if say not in last_seen:
        last_seen[say] = (0, i)
    else:
        gap = i - last_seen[say][1]
        last_seen[say] = (gap, i)

    i += 1

print(say, time.time() - start)
