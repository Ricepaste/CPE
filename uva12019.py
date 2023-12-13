N = int(input())
month_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for _ in range(N):
    M, D = map(int, input().split())
    for i in range(M-1):
        D += month_days[i]
    week_day = D % 7 - 2
    if (week_day <= 0):
        week_day += 7

    if (week_day == 1):
        print("Monday")
    elif (week_day == 2):
        print("Tuesday")
    elif (week_day == 3):
        print("Wednesday")
    elif (week_day == 4):
        print("Thursday")
    elif (week_day == 5):
        print("Friday")
    elif (week_day == 6):
        print("Saturday")
    elif (week_day == 7):
        print("Sunday")
