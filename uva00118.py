MAX_X, MAX_Y = map(int, input().split())
scent = []


def dire_change(now_dire, turn):
    dire_list = ['N', 'E', 'S', 'W']
    if (turn == 'R'):
        turn = 1
    elif (turn == 'L'):
        turn = -1
    return dire_list[(dire_list.index(now_dire) + turn) % 4]


while True:
    try:
        now_x, now_y, dire = input().split()
        now_x = int(now_x)
        now_y = int(now_y)
        command_list = list(input())
        LOST = False

        while (len(command_list) != 0):
            now_cmd = command_list.pop(0)
            if (now_cmd == 'R' or now_cmd == 'L'):
                dire = dire_change(dire, now_cmd)
            elif (now_cmd == 'F'):
                last_x = now_x
                last_y = now_y
                if (dire == 'N'):
                    now_y += 1
                elif (dire == 'E'):
                    now_x += 1
                elif (dire == 'S'):
                    now_y -= 1
                elif (dire == 'W'):
                    now_x -= 1

                if (now_x < 0 or now_y < 0 or now_x > MAX_X or now_y > MAX_Y):
                    # die
                    if ([last_x, last_y] in scent):
                        now_x = last_x
                        now_y = last_y
                        continue
                    scent.append([last_x, last_y])
                    print(last_x, last_y, dire, "LOST")
                    LOST = True
                    break
        if (not (LOST)):
            print(now_x, now_y, dire)

    except:
        break
