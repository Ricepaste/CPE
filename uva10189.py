def solve(fields):
    new_fields = []
    for i in range(len(fields)):
        temp = []
        for j in range(len(fields[i])):
            count = 0

            for det_r in range(max(0, i - 1), min(len(fields), i + 2)):
                for det_c in range(max(0, j - 1), min(len(fields[i]), j + 2)):
                    if (fields[det_r][det_c] == '*'):
                        count += 1
                    elif (fields[det_r][det_c] == '.'):
                        continue
                    else:
                        assert False, "Invalid input"
            if (fields[i][j] == '*'):
                temp.append('*')
            else:
                temp.append(count)
        new_fields.append(temp)

    return new_fields


epoch = 0
first = True
while True:
    try:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        fields = []
        for _ in range(m):
            fields.append(list(input()))

        fields = solve(fields)

        if first:
            first = False
        else:
            print()

        print("Field #{}:".format(epoch+1))
        for i in range(m):
            for j in range(n):
                print(fields[i][j], end='')
            print()

        epoch += 1
    except:
        break
