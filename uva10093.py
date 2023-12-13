def trans(digit):
    digit = str(digit)
    if (digit.isdigit() or (digit <= 'Z' and digit >= 'A')):
        return int(digit, base=36)
    elif (digit <= 'z' and digit >= 'a'):
        return 36 + ord(digit) - ord('a')
    else:
        return None


while True:
    try:
        N = input()
        trans_n = []
        error = False
        succ = False
        naga = False
        if (N[0] == '-'):
            naga = True
            N = N[1:]
        elif (N[0] == '+'):
            N = N[1:]

        for i in N:
            temp = trans(i)
            if (temp is not None):
                trans_n.append(temp)
            else:
                error = True
                break

        if (not (error)):
            # print(trans_n)
            pass
        else:
            print("such number is impossible!")
            continue

        for i in range(max(max(trans_n)+1, 2), 63):
            trans_n_i_based = 0
            power = 1

            for j in trans_n[::-1]:
                trans_n_i_based += power * j
                power *= i

            if (trans_n_i_based % (i-1) == 0):
                print(i)
                succ = True
                break

        if (not (succ)):
            print("such number is impossible!")

    except:
        break
