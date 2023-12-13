testcase = int(input())
for case in range(testcase):
    start_x, start_y, end_x, end_y = map(int, input().split())
    ans = None
    if (start_x + start_y == end_x + end_y):
        ans = start_y - end_y
    elif (start_x + start_y + 1 == end_x + end_y):
        ans = start_y + end_x + 1
    else:
        ans = (((start_x + start_y + 1) + (end_x + end_y - 1)) * ((end_x + end_y - 1) - (start_x +
               start_y + 1) + 1)) / 2 + (end_x + end_y - 1) - (start_x + start_y + 1) + 2 + start_y + end_x
    print("Case {}: {}".format(case+1, int(ans)))
