while True:
    try:
        S, D = map(float, input().split())
        # n_start = (-2*S-1 - (4*S**2 - 4*S + 1 + 8*D)**0.5)/2
        n_end = (-2*S-1 + (4*S**2 - 4*S + 1 + 8*D)**0.5)/2
        if (int(n_end) == n_end):
            print(int(n_end+S))
        else:
            print(int(n_end+S+1))

        # print(n_start+S, n_end+S)
        # print(int(n_start+S), int(n_end+S))
    except:
        break
