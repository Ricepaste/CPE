N = int(input())
MAX = 100000000
fib_s = [1, 2]
l = 0
r = 1
while True:
    temp = fib_s[l] + fib_s[r]
    if (temp < MAX):
        fib_s.append(temp)
    else:
        break
    l += 1
    r += 1

fib_s = fib_s[::-1]

for _ in range(N):
    ori_int = int(input())
    ori_int_cp = ori_int
    trans_int = ""
    i = 0
    while (fib_s[i] > ori_int):
        i += 1
    while (ori_int >= 1 or i < len(fib_s)):
        if (fib_s[i] <= ori_int):
            ori_int -= fib_s[i]
            trans_int += "1"
            i += 1
        else:
            trans_int += "0"
            i += 1
    print("{} = {} (fib)".format(ori_int_cp, trans_int))
