N = int(input())
for _ in range(N):
    ori_data = int(input())
    print("{} {}".format(str(bin(ori_data))[2:].count('1'), str(
        bin(int('0x' + str(ori_data), base=16))).count('1')))
