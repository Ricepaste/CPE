import math

while True:
    try:
        r, a, unit = input().split()
        r = float(r) + 6440.
        if (unit == 'deg'):
            a = float(a)
        elif (unit == 'min'):
            a = float(a) / 60.

        while a >= 360:
            a -= 360

        if (a >= 180):
            a = 360 - a
        # print(r, a)
        # print(round(math.radians(a) * r, ndigits=6), end=' ')
        # print(round(2 * r * math.sin(math.radians(a/2.)), ndigits=6))
        print("{:.6f} {:.6f}".format(math.radians(a) * r,
              2 * r * math.sin(math.radians(a/2.))))
    except:
        break
