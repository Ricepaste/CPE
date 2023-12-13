while True:
    try:
        n = int(input())
        all_num = []
        for _ in range(n):
            all_num.append(int(input()))
        all_num.sort()

        mid1 = len(all_num) // 2 - 1
        mid2 = len(all_num) // 2

        if (len(all_num) % 2 == 0 and (all_num[mid1] != all_num[mid2])):
            valid_num = all_num.count(
                all_num[mid1]) + all_num.count(all_num[mid2])
            pos_num = all_num[mid2] - all_num[mid1] + 1
        else:
            valid_num = all_num.count(all_num[mid1]) if len(
                all_num) % 2 == 0 else all_num.count(all_num[mid2])
            pos_num = 1
        A = all_num[mid1] if len(all_num) % 2 == 0 else all_num[mid2]
        print("{} {} {}".format(A, valid_num, pos_num))

    except:
        break
