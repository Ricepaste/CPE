while True:
    testcase = int(input())
    if (testcase == 0):
        break

    top = 1
    north = 2
    west = 3
    east = 4
    south = 5
    bottom = 6

    for _ in range(testcase):
        cmd = input()
        if cmd == "north":
            top, north, west, east, south, bottom = south, top, west, east, bottom, north
        elif cmd == "east":
            top, north, west, east, south, bottom = west, north, bottom, top, south, east
        elif cmd == "south":
            top, north, west, east, south, bottom = north, bottom, west, east, top, south
        elif cmd == "west":
            top, north, west, east, south, bottom = east, north, top, bottom, south, west
    print(top)
