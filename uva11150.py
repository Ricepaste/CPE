def solve(cola_new, cola_old):
    cola_borrow = cola_old
    cola_all = cola_new
    cola_old += cola_new
    cola_new = 0

    while cola_old >= 3:
        cola_new = cola_old // 3
        cola_all += cola_new
        cola_old = cola_old % 3 + cola_new
        if (cola_old == cola_borrow):
            break

    return cola_all, cola_old


while True:
    try:
        cola_new = int(input())
        max = 0
        # for i in range(2):
        #     cola_all, cola_old = solve(cola_new, i)
        # if (cola_all > max and (i == cola_old or i == 0)):
        #     max = cola_all
        borrow = 0 if cola_new % 2 == 1 else 2
        cola_all, cola_old = solve(cola_new, borrow)
        if (cola_old == borrow or borrow == 0):
            print(cola_all)

        # print(max)
    except:
        break
