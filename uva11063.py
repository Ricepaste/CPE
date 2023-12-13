case = 0
while True:
    try:
        _ = int(input())
        seq = list(map(int, input().split()))

        sort_same = True
        sort_seq = sorted(seq)
        for i in range(len(seq)):
            if (seq[i] != sort_seq[i]):
                sort_same = False
                break
        if (not (sort_same)):
            case += 1
            print("Case #{}: It is not a B2-Sequence.".format(case))
            print()
            _ = input()
            continue

        sum_set = set()

        b2_seq = True

        for L in range(len(seq)):
            for R in range(L, len(seq)):
                if (seq[L] + seq[R] in sum_set or seq[0] < 1):
                    b2_seq = False
                    break
                else:
                    sum_set.add(seq[L] + seq[R])
            if (not (b2_seq)):
                break

        case += 1
        print("Case #{}: It is{} a B2-Sequence.".format(case, '' if b2_seq else " not"))
        print()

        _ = input()
    except:
        break
