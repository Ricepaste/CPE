import sys

N = int(input())
_ = input()
second_output = False

for case in range(N):
    tree = {}
    tree_nums = 0

    while True:
        temp = sys.stdin.readline().strip()
        if (temp == ''):
            break

        tree[temp] = tree.get(temp, 0) + 1
        tree_nums += 1

    if (second_output):
        print()

    tree = dict(sorted(tree.items(), key=lambda x: x[0]))
    for key, value in tree.items():
        ans = f"{value / tree_nums * 100:.4f}"
        print(f"{key} {ans}")

    second_output = True
