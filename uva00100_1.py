cycle_times = {}

while True:
    try:
        i, j = map(int, input().split())

        max_cycles = 0
        for num in range(min(i, j), max(i, j)+1):
            cycle = 1
            n = num
            while n != 1:
                if n in cycle_times:
                    cycle += cycle_times[n] - 1
                    break
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = 3 * n + 1
                cycle += 1

            if cycle > max_cycles:
                max_cycles = cycle

            cycle_times[num] = cycle
        print(i, j, max_cycles)
    except:
        break

# print(cycle_times)
