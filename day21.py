with open('input21.txt') as f:
    inputs = f.readlines()

allergen_ingred = {}
ingredient_counts = {}
for line in inputs:
    ingred, aller = line.split(' (contains ')
    allergens = aller[:-2].split(', ')
    ingredients = set(ingred.split())
    for ingredient in ingredients:
        if ingredient not in ingredient_counts.keys():
            ingredient_counts[ingredient] = 1
        else:
            ingredient_counts[ingredient] += 1
    for allergen in allergens:
        if allergen in allergen_ingred.keys():

            allergen_ingred[allergen] = allergen_ingred[allergen].intersection(ingredients)
        else:
            allergen_ingred[allergen] = ingredients

bad_ingred = set()
for value in allergen_ingred.values():
    bad_ingred.update(value)

total = 0
for key, count in ingredient_counts.items():
    if key not in bad_ingred:
        total += count
print(total)

allergen_matches = {}
while bad_ingred:
    match = min(allergen_ingred.items(), key=lambda x: len(x[1]))
    allergen = match[0]
    choices = match[1]
    match = choices.pop()
    allergen_matches[allergen] = match
    bad_ingred -= {match}
    del allergen_ingred[allergen]
    for allergen in allergen_ingred.keys():
        allergen_ingred[allergen] -= {match}

match_list = [x[1] for x in sorted(allergen_matches.items())]
print(','.join(match_list))