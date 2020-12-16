with open('input16.txt') as f:
    inputs = f.readlines()

end_of_rules = inputs.index('\n')
rules = inputs[:end_of_rules]

my_ticket = inputs[end_of_rules + 2]

tickets = inputs[end_of_rules + 5:]

rate = 0
valid_entries = set()
for line in rules:
    field, values = line.split(': ')
    ranges = values.split(' or ')
    for pair in ranges:
        a, b = pair.split('-')
        for num in range(int(a), int(b) + 1):
            valid_entries.add(num)

for ticket in tickets:
    nums = ticket.split(',')
    for num in nums:
        if int(num) not in valid_entries:
            rate += int(num)

print(rate)
