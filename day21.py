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
    # print(len(value))
    bad_ingred.update(value)

# print(len(bad_ingred), len(allergen_ingred))
total = 0
for key, count in ingredient_counts.items():
    if key not in bad_ingred:
        total += count
print(total)
