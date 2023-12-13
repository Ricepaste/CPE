N = int(input())
country_dict = {}
for _ in range(N):
    beauties = list(input().split())
    beauty_country = beauties[0]
    if (country_dict.get(beauty_country) is None):
        country_dict[beauty_country] = 1
    else:
        country_dict[beauty_country] += 1

for key, value in sorted(country_dict.items()):
    print(key, value)
