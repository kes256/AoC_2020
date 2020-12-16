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

valid_tickets = [my_ticket]
for ticket in tickets:
    valid = True
    nums = ticket.split(',')
    for num in nums:
        if int(num) not in valid_entries:
            rate += int(num)
            valid = False
    if valid:
        valid_tickets.append(ticket)

print(rate)

rules_dict = {}

for line in rules:
    field, values = line.split(': ')
    rules_dict[field] = set()
    ranges = values.split(' or ')
    for pair in ranges:
        a, b = pair.split('-')
        for num in range(int(a), int(b) + 1):
            rules_dict[field].add(num)

field_count = len(rules_dict)
matching = {field: {i: 0 for i in range(field_count)} for field in rules_dict.keys()}

for ticket in valid_tickets:
    nums = ticket.split(',')
    i = 0
    for num in nums:
        for field in rules_dict.keys():
            if int(num) not in rules_dict[field]:
                matching[field][i] += 1
        i += 1

for field in matching.keys():
    matches = [index for index, count in matching[field].items() if count == 0]
    matching[field] = matches
sorted_matches = sorted([(len(value), key, value) for key, value in matching.items()])
assigned_cols = set()

field_to_col = {}
for length, field, cols in sorted_matches:
    available_col = min(set(cols) - assigned_cols)
    field_to_col[field] = available_col
    assigned_cols.add(available_col)

prod = 1
my_fields = my_ticket.split(',')
for key in field_to_col.keys():
    if 'departure' not in key:
        continue
    prod *= int(my_fields[field_to_col[key]])
print(prod)
