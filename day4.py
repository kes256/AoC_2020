import re

with open('input4.txt') as f:
    inputs = f.read()

passport_list = inputs.split('\n\n')
fields = {'byr': [re.compile('\d{4}'), 1920, 2002],
          'iyr': [re.compile('\d{4}'), 2010, 2020],
          'eyr': [re.compile('\d{4}'), 2020, 2030],
          'hgt': [re.compile('\d+(in)|(cm)'), {'in': [59, 76], 'cm': [150, 193]}],
          'hcl': [re.compile('#[0-9a-f]{6}'),],
          'ecl': [re.compile('(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)'),],
          'pid': [re.compile('\d{9}'),]}

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
