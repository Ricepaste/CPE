S = int(input())
for _ in range(S):
    N, p, i = map(float, input().split())
    N = int(N)
    i = int(i)
    q = 1-p
    mul = q ** N

    curr_rate = (p * q**(i-1)) / (1. - mul)
    print("{:.4f}".format(round(curr_rate, 4)))
