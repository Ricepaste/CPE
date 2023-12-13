b4 = False
while True:
    try:
        ascii_times = {}
        lines = list(input())
        if (b4):
            print()
        for i in lines:
            if (ascii_times.get(ord(i)) is None):
                ascii_times[ord(i)] = 1
            else:
                ascii_times[ord(i)] += 1

        sort_dic = dict(sorted(ascii_times.items(), reverse=True))
        sort_dic = dict(sorted(sort_dic.items(), key=lambda x: x[1]))
        # print(sort_dic.items())

        for key, value in sort_dic.items():
            print(key, value)
        b4 = True
    except:
        break
