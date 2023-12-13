while True:
    try:
        n = int(input())
        if (n == 0):
            break

        print("The parity of {} is {} (mod 2).".format(
            str(bin(n))[2:], bin(n).count('1')))
    except:
        break
