ripple = [800, 900, 950, 970, 980]
ripple_dict = {"2/21": 800, "2/22": 900, "2/23": 950, "2/24": 970, "2/25": 980}
total = 0
for x in ripple_dict.values():
    total += x

total /= 5
print(total)
