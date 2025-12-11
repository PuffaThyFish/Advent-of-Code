
def getFreshIngredients(file_path):
    with open(file_path, 'r') as database:
        database_list = database.read().splitlines()
        split_index = database_list.index('')
        fresh_ranges = database_list[:split_index]
        ingredients = database_list[split_index+1:]
        fresh_ingredients = countFreshIngredients(fresh_ranges, ingredients)
    return fresh_ingredients

def countFreshIngredients(fresh_ranges, ingredients):
    fresh = dict() # lo: hi
    for fresh_range in fresh_ranges:
        split_index = fresh_range.find('-')
        lo = int(fresh_range[:split_index])
        hi = int(fresh_range[split_index+1:])
        fresh[lo] = hi

    fresh_ingredients = 0
    for ingredient in ingredients:
        ingredient = int(ingredient)
        for lo in fresh:
            if lo <= ingredient and fresh[lo] >= ingredient:
                fresh_ingredients += 1
                print(f'{lo} < {ingredient} < {fresh[lo]}')
                break
    return fresh_ingredients

print(getFreshIngredients(r"2025\day5\test.txt"))
print(getFreshIngredients("2025\day5\input.txt"))