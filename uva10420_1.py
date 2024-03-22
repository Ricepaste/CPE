country_count = {}

n = int(input())
for i in range(n):
    country = input().split()[0]
    if country not in country_count:
        country_count[country] = 1
    else:
        country_count[country] += 1

for country, times in sorted(country_count.items(), key=lambda x: x[0]):
    print(country, times)
