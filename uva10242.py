while True:
    try:
        temp = list(map(float, input().split()))
        point_l = [temp[0:2], temp[2:4], temp[4:6], temp[6:8]]
        for a in range(len(point_l)):
            for b in range(a + 1, len(point_l)):
                if (point_l[a] == point_l[b]):
                    if (a == 0):
                        point_l[0], point_l[1] = point_l[1], point_l[0]
                    if (b == 3):
                        point_l[2], point_l[3] = point_l[3], point_l[2]

        print("{:.3f} {:.3f}".format(point_l[0][0] + (point_l[3][0] - point_l[2][0]),
              point_l[0][1] + (point_l[3][1] - point_l[2][1])))
    except:
        break
