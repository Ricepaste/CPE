while True:
    try:
        n, m = map(int, input().split())
        boring = True
        seq = []
        seq.append(n)

        if (n != 0 and n != 1 and m != 0 and m != 1):
            mod = n % m
            while (mod == 0):
                temp = n // m
                seq.append(temp)
                if (temp == 1):
                    boring = False
                    break
                n = temp
                mod = n % m
        if (not (boring)):
            print(" ".join(list(map(str, seq))))
        else:
            print("Boring!")

    except:
        break
