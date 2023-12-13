epoch = int(input())
for _ in range(epoch):
    all_num = list(map(int, input().split()))
    # print(all_num)
    num = all_num[0]
    all_num = all_num[1:]

    all_num.sort()
    mid = all_num[num//2]
    dist = []
    for i in all_num:
        dist.append(abs(mid-i))
    print(sum(dist))
