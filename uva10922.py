while True:
    try:
        data = input()
        data_b = data
        if (data == '0'):
            break

        nine_degree = 0 if data != '9' else 1

        while (len(data) > 1):
            nine_degree += 1
            data = list(map(int, list(data)))
            data = str(sum(data))

        if data == '9':
            print(
                "{} is a multiple of 9 and has 9-degree {}.".format(data_b, nine_degree))
        else:
            print("{} is not a multiple of 9.".format(data_b))

    except:
        break
