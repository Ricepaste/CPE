while True:
    try:
        N, M = map(int, input().split())
        print(N, M)
        if (N == 0 and M == 0):
            break
        all_value = []
        for _ in range(N):
            all_value.append(int(input()))

        # all_value.sort(key=lambda x: (
        #     x % M, -(x % 2), x if x % 2 == 0 else -x))
        all_value.sort(key=lambda x: x if x % 2 == 0 else -x)
        all_value.sort(key=lambda x: -(x % 2))
        all_value.sort(key=lambda x: x % M)
        # print(all_value)

        # for i in range(len(all_value)):
        #     for j in range(len(all_value) - i - 1):
        #         if (all_value[j] % M == all_value[j+1] % M):
        #             if (all_value[j] % 2 == 0 and all_value[j+1] % 2 == 1):
        #                 # print('Cur:', all_value)
        #                 all_value[j], all_value[j +
        #                                         1] = all_value[j+1], all_value[j]
        # # print(all_value)

        # for i in range(len(all_value)):
        #     for j in range(len(all_value) - i - 1):
        #         if (all_value[j] % M == all_value[j+1] % M):
        #             if (all_value[j] % 2 == 1 and all_value[j+1] % 2 == 1):
        #                 if (all_value[j] < all_value[j+1]):
        #                     all_value[j], all_value[j +
        #                                             1] = all_value[j+1], all_value[j]

        # for i in range(len(all_value)):
        #     for j in range(len(all_value) - i - 1):
        #         if (all_value[j] % M == all_value[j+1] % M):
        #             if (all_value[j] % 2 == 0 and all_value[j+1] % 2 == 0):
        #                 if (all_value[j] > all_value[j+1]):
        #                     all_value[j], all_value[j +
        #                                             1] = all_value[j+1], all_value[j]

        all_value = list(map(str, all_value))
        print("\n".join(all_value))
    except:
        break
