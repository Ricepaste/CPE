while True:
    try:
        a, b = map(int, input().split())
        if (a == b and a == 0):
            break
        count = 0
        curr_num = 1
        while (True):
            if curr_num ** 2 < a:
                curr_num += 1
            else:
                break
        while (True):
            if (curr_num ** 2 >= a and curr_num ** 2 <= b):
                count += 1
                curr_num += 1
            else:
                break
        print(count)
    except:
        break
