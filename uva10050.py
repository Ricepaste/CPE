testtimmes = int(input())
for _ in range(testtimmes):
    days = int(input())
    partys = int(input())
    hartal_all_sets = set()
    for _2 in range(partys):
        restdays = int(input())
        hartal = set()
        mul = 0
        while mul * restdays <= days:
            if (mul * restdays % 7 == 0) or (mul * restdays % 7 == 6):
                mul += 1
                continue
            else:
                hartal.add(mul * restdays)
                mul += 1
            # print(mul)
        hartal_all_sets.update(hartal)
    print(len(hartal_all_sets))
