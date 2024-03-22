ary = []
longest = 0

while True:
    try:

        temp = list(input())
        if len(temp) == 0 or temp[0] == '\0' or temp[0] == '\n':
            break
        if len(temp) > longest:
            longest = len(temp)

        # if (temp[0] == '\0'):
        #     break
        for i in range(100 - len(temp)):
            temp.append(' ')

        ary.append(temp)

    except:
        break

for i in range(longest):
    for j in range(len(ary)-1, -1, -1):
        print(ary[j][i], end='')
    print()
