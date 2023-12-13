while True:
    try:
        jolly = True

        test_data = list(map(int, input().split()))[1:]
        sep_data = []
        for i in range(len(test_data)-1):
            sep_data.append(abs(test_data[i]-test_data[i+1]))
        sep_data.sort()

        # print(sep_data)
        for i in range(len(sep_data)):
            if (i+1 != sep_data[i]):
                print("Not jolly")
                jolly = False
                break
        if (jolly):
            print("Jolly")
    except:
        break
