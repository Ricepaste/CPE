while True:
    try:
        a, b = map(int, input().split())
        c = (a-b) if a > b else (b-a)
        print(c)
    except:
        break
