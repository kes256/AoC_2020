import re

with open('input19.txt') as f:
    inputs = f.readlines()

message_start = 0
rules = {}
rule_lookups = {}
for index, line in enumerate(inputs):
    if line == '\n':
        message_start = index
        break
    rule, contents = line.strip().split(': ')
    if rule not in rule_lookups.keys():
        rule_lookups[rule] = set()
    rules[rule] = f' {contents} '
    nums = contents.replace('|', '').split()
    for num in nums:
        if num in rule_lookups.keys():
            rule_lookups[num].add(rule)
        else:
            rule_lookups[num] = {rule}

reference = re.compile('\d+')
flat_rules = {*rule_lookups['"a"'], *rule_lookups['"b"']}
while flat_rules:
    current_rule = flat_rules.pop()
    content = rules[current_rule].replace('"', '')
    for rule in rule_lookups[current_rule]:
        rules[rule] = rules[rule].replace(f' {current_rule} ', f' ({content}) ')
        rules[rule] = rules[rule].replace(f' {current_rule} ', f' ({content}) ')
        rules[rule] = rules[rule].replace(f' {current_rule} ', f' ({content}) ')
        rules[rule] = rules[rule].replace(f' {current_rule} ', f' ({content}) ')
        # print(f'{current_rule} -> {rule}: {rules[rule]}')
        if not reference.search(rules[rule]):
            flat_rules.add(rule)

rule_zero = rules['0'].replace(' ', '')
match_zero = re.compile(f'^{rule_zero}$')

count = 0
for line in inputs[message_start + 1:]:
    if match_zero.search(line):
        count += 1

print(count)


rules['8'] = ' 42 | 42 8 '
rules['11'] = ' 42 31 | 42 11 31 '

