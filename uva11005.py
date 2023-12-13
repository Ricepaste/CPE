N = int(input())
for i in range(N):
    cost_table = []
    print('Case {}:'.format(i+1))
    for _ in range(4):
        temp = list(map(int, input().split()))
        cost_table += temp

    queries_num = int(input())
    for _ in range(queries_num):
        query = int(input())
        all_cost = []
        all_cost_base = []

        for base in range(2, 37):
            cost = 0
            query_temp = query
            while (query_temp > 0):
                cost += cost_table[query_temp % base]
                query_temp //= base
            all_cost.append(cost)
            all_cost_base.append(base)
        # print(all_cost)
        # print(all_cost_base)

        min_base = []
        min_cost = min(all_cost)
        while (min_cost in all_cost):
            min_base.append(all_cost_base.pop(all_cost.index(min_cost)))
            all_cost.pop(all_cost.index(min_cost))

        print("Cheapest base(s) for number {}:".format(query), end='')
        for ans in min_base:
            print(' ', ans, sep='', end='')
        print()
    if (i != N-1):
        print()
