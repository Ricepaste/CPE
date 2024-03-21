while True:
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break

    carry = 0
    times = 0
    while (a > 0 or b > 0):
        carry = a % 10 + b % 10 + carry
        a //= 10
        b //= 10
        carry //= 10
        if carry:
            times += 1

    if not (times):
        print("No carry operation.")
    elif times == 1:
        print("1 carry operation.")
    else:
        print(f"{times} carry operations.")
