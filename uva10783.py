N = int(input())
for i in range(N):
    start = int(input())
    end = int(input())
    start = start if start % 2 == 1 else start + 1
    end = end if end % 2 == 1 else end - 1
    n = (end - start) / 2 + 1
    print("Case {}: {}".format(i+1, int((start + end) * n / 2)))
