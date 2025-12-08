
def getFreshIngredients(file_path):
    with open(file_path, 'r') as database:
        database_list = database.read().splitlines()
        for line in database_list:
            print(line)
        split_index = database_list.index('')
        fresh_ranges = database_list[:split_index]
        ingredients = database_list[split_index+1:]
        fresh_ingredients = countFreshIngredients(fresh_ranges, ingredients)
    return fresh_ingredients

def countFreshIngredients(fresh_ranges, ingredients):
    fresh = set()
    for fresh_range in fresh_ranges:
        split_index = fresh_range.find('-')
        lo = int(fresh_range[:split_index])
        hi = int(fresh_range[split_index+1:])
        for num in range(lo, hi+1):
            fresh.add(num)

    print('set')
    print(fresh)
    
    fresh_ingredients = 0
    for ingredient in ingredients:
        if ingredient in fresh:
            fresh_ingredients += 1
    return fresh_ingredients

#print(getFreshIngredients(r"2025\day4\test.txt"))
print(getFreshIngredients("2025\day5\input.txt"))