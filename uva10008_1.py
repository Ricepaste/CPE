text = ""
alpha_count = {}

n = int(input())

for _ in range(n):
    text += input().upper()

for t in text:
    if t.isalpha():
        if t not in alpha_count:
            alpha_count[t] = 1
        else:
            alpha_count[t] += 1

new_dict = {}

for alpha, times in sorted(alpha_count.items(), key=lambda x: x[0], reverse=0):
    new_dict[alpha] = times

for alpha, times in sorted(new_dict.items(), key=lambda x: x[1], reverse=1):
    print(alpha, times)
