N = int(input())
for case in range(N):
    L = int(input())
    train = list(map(int, input().split()))

    swap = 0
    for i in range(L):
        for j in range(L-i-1):
            if (train[j] > train[j+1]):
                swap += 1
                train[j], train[j+1] = train[j+1], train[j]
    print("Optimal train swapping takes {} swaps.".format(swap))
