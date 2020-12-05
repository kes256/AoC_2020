import re

with open('input4.txt') as f:
    inputs = f.read()

passport_list = inputs.split('\n\n')
fields = {'byr': [re.compile('^\d{4}$'), 1920, 2002],
          'iyr': [re.compile('^\d{4}$'), 2010, 2020],
          'eyr': [re.compile('^\d{4}$'), 2020, 2030],
          'hgt': [re.compile('^\d+((in)|(cm))$'), {'in': [59, 76], 'cm': [150, 193]}],
          'hcl': [re.compile('^#[0-9a-f]{6}$'),],
          'ecl': [re.compile('^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$'),],
          'pid': [re.compile('^\d{9}$'),]}

count = 0
for line in passport_list:
    invalid = False
    for key in fields.keys():
        if key in line:
            pass
        else:
            invalid = True
    if not invalid:
        count += 1

print(count)

count = 0
for line in passport_list:
    invalid = False
    for key in fields.keys():
        if key in line:
            pass
        else:
            invalid = True

    pairs = line.split()

    entries = [pair.split(':') for pair in pairs]
    for pair in entries:
        if invalid:
            break
        key, value = pair
        if key in fields.keys():
            match = fields[key][0].match(value)
            if not match:
                invalid = True
                break
            if len(fields[key]) == 3:
                if not fields[key][1] <= int(value) <= fields[key][2]:
                    invalid = True
                    break
            if len(fields[key]) == 2:
                units = match[1]
                min_val = fields[key][1][units][0]
                max_val = fields[key][1][units][1]
                value = value.strip(units)
                if not min_val <= int(value) <= max_val:
                    invalid = True
                    break

    if not invalid:
        count += 1

print(count)
