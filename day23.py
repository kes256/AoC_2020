import time

start_time = time.time()
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
answer = ''
for i in result:
    answer += f'{i}'
print(answer, time.time() - start_time)
start_time = time.time()


class Cup:
    def __init__(self, value, prev_cup, next_cup, one_down):
        self.label = value
        self.prev = prev_cup
        self.next = next_cup
        self.prev_label = one_down

    def __repr__(self):
        if self.next:
            next_label = self.next.label
        else:
            next_label = 'none'

        if self.prev:
            prev_label = self.prev.label
        else:
            prev_label = 'none'

        if self.prev_label:
            one_down = self.prev_label.label
        else:
            one_down = 'none'

        return f'{self.label}'#', next cup: {next_label}, prev cup: {prev_label}, one down: {one_down}'


def join_cups(cup_a, cup_b):
    cup_a.next = cup_b
    cup_b.prev = cup_a


def game(size, duration):
    input = [int(num) for num in '123487596']
    cup_one = Cup(input[0], None, None, None)
    prev_cup = cup_one
    cups_to_index = [cup_one]
    labels_to_find = [cup_one.label - 1]
    for i in range(size - 1):
        if i < 8:
            num = input[i+1]
        else:
            num = i + 2
        if prev_cup.label == num - 1:
            one_down = prev_cup
        else:
            one_down = None
        current_cup = Cup(num, prev_cup, None, one_down)
        if num in labels_to_find:
            index = labels_to_find.index(num)
            labels_to_find.pop(index)
            to_update = cups_to_index.pop(index)
            to_update.prev_label = current_cup
        if not one_down:
            cups_to_index.append(current_cup)
            labels_to_find.append(num - 1)
        prev_cup.next = current_cup
        prev_cup = current_cup
    print(f'created all cups: {time.time() - start_time}')
    for cup in cups_to_index:
        num = cup.label - 1
        if num == 0:
            num = size
            if prev_cup.label == num:
                cup.prev_label = prev_cup
                continue
        cup_to_check = cup_one
        while True:
            if cup_to_check.label == num:
                cup.prev_label = cup_to_check
                break
            cup_to_check = cup_to_check.next
    print(f'finished matching cups with previous labels: {time.time() - start_time}')
    cup_one.prev = prev_cup
    prev_cup.next = cup_one
    current_cup = cup_one
    for i in range(duration):
        three_cups = [current_cup.next]
        three_cups.append(three_cups[-1].next)
        three_cups.append(three_cups[-1].next)
        next_cup = three_cups[-1].next
        start_cup = current_cup.prev_label
        while start_cup in three_cups:
            start_cup = start_cup.prev_label
        end_cup = start_cup.next
        join_cups(current_cup, next_cup)
        join_cups(start_cup, three_cups[0])
        join_cups(three_cups[-1], end_cup)
        current_cup = next_cup
    return cup_one


cup = game(1000000, 10000000)
answer = 1
for _ in range(2):
    cup = cup.next
    answer *= cup.label
print(answer, time.time() - start_time)
