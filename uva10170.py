while True:
    try:
        X = int(input())
        coef = list(map(int, input().split()))
        for i in range(len(coef) - 1):
            now_coef_old = len(coef) - i - 1
            coef[i] *= now_coef_old
        coef.pop()
        # print(coef)

        poly = 1
        sum = 0
        for i in range(len(coef)-1, -1, -1):
            sum += poly * coef[i]
            poly *= X
        print(sum)
    except:
        break
