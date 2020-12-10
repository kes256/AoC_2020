from itertools import groupby
with open('input10.txt') as f:
    inputs = f.readlines()

ints = [int(x) for x in inputs]

ordered = sorted(ints)
diffs = [ordered[i] - ordered[i - 1] for i in range(len(ordered))]
diffs[0] = ordered[0]
diffs.append(3)

ones = diffs.count(1)
threes = diffs.count(3)

print(ones * threes)

sublists = [list(group) for k, group in groupby(diffs, lambda x: x == 3) if not k]
runs = [len(x) for x in sublists]
print(max(runs))  # longest stretch between a required jump of 3 jolts is 4


def count_adapter_options(ordered_list):
    length = len(ordered_list)
    diff = (ordered_list[-1] - ordered_list[0])
    count = 0
    if length < 3:
        count = 1
    elif diff <= 3:
        count = 2 ** (length - 2)
    elif diff == 4:
        count =  2 ** (length - 2) - 1
    else:
        print('This gap was too big!')
    return count


ordered = [0] + ordered + [ordered[-1] + 3]
choices = []
start = 0
stop = 0
for i in range(len(ordered) - 1):
    if (ordered[i + 1] - ordered[i]) == 3:
        stop = i + 1
        choices.append(count_adapter_options(ordered[start:stop]))
        start = stop

final_count = 1
for num in choices:
    final_count *= num
print(final_count)
