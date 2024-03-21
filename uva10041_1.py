r = int(input())
for i in range(r):
    neighbors = list(map(int, input().split()))[1:]
    neighbors.sort()

    # if len(neighbors) % 2 == 0:
    #     mid = len(neighbors) // 2
    #     mid_1 = len(neighbors) // 2 - 1
    #     sums = 0
    #     sums_1 = 1

    #     for i in range(len(neighbors)):
    #         sums += abs(neighbors[mid] - neighbors[i])
    #     for i in range(len(neighbors)):
    #         sums_1 += abs(neighbors[mid_1] - neighbors[i])

    #     print(sums)
    # else:
    mid = len(neighbors) // 2
    sums = 0

    for i in range(len(neighbors)):
        if i != mid:
            sums += abs(neighbors[mid] - neighbors[i])

    print(sums)
