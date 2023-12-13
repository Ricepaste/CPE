while True:
    try:
        N = input()
        if (N == '0'):
            break
        while (len(N) > 1):
            sum = 0
            for i in N:
                sum += int(i)
            N = str(sum)
        print(N)
    except:
        break
