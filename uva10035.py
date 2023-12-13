while (True):
    a, b = map(int, input().split())
    if (a == b and a == 0):
        break
    carry_times = 0
    carry = 0
    while (a > 0 or b > 0):
        carry = (a % 10 + b % 10 + carry) // 10
        if carry == 1:
            carry_times += 1
        a //= 10
        b //= 10
    if (carry_times == 0):
        print("No carry operation.")
    elif (carry_times == 1):
        print("{} carry operation.".format(carry_times))
    else:
        print("{} carry operations.".format(carry_times))
