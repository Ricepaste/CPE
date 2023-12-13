def GCD(a, b):
    # b is bigger than a
    global mem
    while True:
        if (a == 0 and b != 0):
            return b
        else:
            temp = b % a
            b = a
            a = temp


mem = []
for i in range(1, 500):
    temp = []
    for j in range(i+1, 501):
        temp.append(GCD(i, j))
    mem.append(temp)

while True:
    try:
        N = int(input())
        if (N == 0):
            break
        G = 0
        for i in range(1, N):
            for j in range(i+1, N+1):
                G += mem[i-1][j-i-1]
        print(G)
    except:
        break
