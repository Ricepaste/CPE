while True:
    try:
        a, b = map(int, input().split())
        print(abs(a-b))
    except:
        break
