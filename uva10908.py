def is_square(r, c, l, sq_map):
    half = (l - 1) // 2

    for x in range(r - half, r + half + 1):
        for y in range(c - half, c + half + 1):
            if (x < 0 or x >= M or y < 0 or y >= N or sq_map[x][y] != sq_map[r][c]):
                return False
    return True


T = int(input())

for testcase in range(T):
    M, N, Q = map(int, input().split())
    print(M, N, Q)
    sq_map = []
    for row in range(M):
        sq_map.append(list(input()))
    for ct_case in range(Q):
        r, c = map(int, input().split())

        max_l = 1
        for l in range(1, min(M, N)+1, 2):
            if (not (is_square(r, c, l, sq_map))):
                break
            else:
                max_l = l
        print(max_l)
