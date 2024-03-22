while True:
    try:
        a = list(input())
        b = list(input())
        intersection = []
        while a != []:
            temp = a.pop()
            if temp in b:
                intersection.append(temp)
                b.pop(b.index(temp))
        intersection = sorted(intersection)
        print(''.join(intersection))

    except:
        break
