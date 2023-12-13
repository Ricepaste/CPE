N = int(input())
for _ in range(N):
    s, d = map(int, input().split())
    a = (s+d)/2
    b = (s-d)/2
    if (a >= 0 and b >= 0 and a == int(a) and b == int(b)):
        print(int(a), int(b))
    else:
        print('impossible')
