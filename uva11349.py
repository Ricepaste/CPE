N = int(input())
for times in range(N):
    matrix = []
    _, _, dim = input().split()
    dim = int(dim)
    for _ in range(dim):
        matrix.append(list(map(int, input().split())))

    sym = True
    for row in range(dim):
        for col in range(dim):
            row_t = dim - 1 - row
            col_t = dim - 1 - col
            if (matrix[row][col] != matrix[row_t][col_t] or matrix[row][col] < 0):
                sym = False
                break
            if (row > dim // 2 and col > dim // 2):
                break
    if (sym):
        print("Test #{}: Symmetric.".format(times+1))
    else:
        print("Test #{}: Non-symmetric.".format(times+1))
    # print(matrix)
