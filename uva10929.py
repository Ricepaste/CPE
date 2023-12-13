i = 1
while True:
    try:
        N = int(input())
        title = "{}. ".format(i)
        output = ""
        Done = False
        sepp = 1

        if (N == 0):
            output = '0'
            Done = True

        while (not Done):
            if (N % 100 != 0):
                output = str(N % 100) + output
                sepp = 1
            N //= 100
            if (N >= 1):
                if (N % 10 != 0):
                    output = str(N % 10) + " shata" + sepp * ' ' + output
                    sepp = 1
            N //= 10
            if (N >= 1):
                if (N % 100 != 0):
                    output = str(N % 100) + " hajar" + sepp * ' ' + output
                    sepp = 1
            N //= 100
            if (N >= 1):
                if (N % 100 != 0):
                    output = str(N % 100) + " lakh" + sepp * ' ' + output
                    sepp = 1
            N //= 100
            if (N >= 1):
                if (N % 100 != 0 and N < 100):
                    output = str(N % 100) + " kuti" + sepp * ' ' + output
                    sepp = 1
                elif (N >= 100):
                    output = " kuti " + output
            if (N < 100):
                Done = True
            else:
                sepp = 0
        i += 1

        print(title + output)

    except:
        break
