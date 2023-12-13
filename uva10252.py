all_sen = []

while True:
    try:
        temp = list(input())
        all_sen.append(temp)

    except:
        break
# print(all_sen)

max_len = 0
for _ in range(len(all_sen)):
    if len(all_sen[_]) > max_len:
        max_len = len(all_sen[_])

# print(all_sen)
for i in range(max_len):
    for j in range(len(all_sen)-1, -1, -1):
        if (len(all_sen[j]) == 0):
            print(" ", end='')
            continue
        if (len(all_sen[j]) < i+1):
            print(" ", end='')
            continue
        print(all_sen[j][i], end='')
    print()
