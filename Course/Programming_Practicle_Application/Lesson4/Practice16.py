dishes = {'Spaghetti Carbonara': ['pasta', 'eggs', 'onions', 'chicken'],'Chicken Curry': ['chicken', 'coconut milk', 'curry powder', 'onions', 'eggs']}
times_cnt = {}
for ingredients in dishes.values():
    for ingredient in ingredients:
        if ingredient in times_cnt:
            times_cnt[ingredient] += 1
        else:
            times_cnt[ingredient] = 1
print(times_cnt)