N = int(input())
temp_input = ""
alpha_dict = {}

for _ in range(N):
    temp_input += input()
temp_input = temp_input.lower()

for i in temp_input:
    if (i.isalpha()):
        if (alpha_dict.get(i) is None):
            alpha_dict[i] = 1
        else:
            alpha_dict[i] += 1

new_dict = {}
# print(alpha_dict)
for key, value in sorted(alpha_dict.items(), key=lambda alpha_dict: alpha_dict[0]):
    new_dict[key] = value

for key, value in sorted(new_dict.items(), key=lambda new_dict: new_dict[1], reverse=True):
    print(key.upper(), value)
