N = int(input())
for pair in range(1, N+1):
    s1 = int(input(), base=2)
    s2 = int(input(), base=2)
    s1, s2 = (s1, s2) if s1 > s2 else (s2, s1)

    left = s1 % s2
    while (left != 0):
        s1 = s2
        s2 = left
        left = s1 % s2

    if (s2 != 1):
        print("Pair #{}: All you need is love!".format(pair))
    else:
        print("Pair #{}: Love is not all you need!".format(pair))
