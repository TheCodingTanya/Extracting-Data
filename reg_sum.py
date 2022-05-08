import re
sum = 0
hand = open('regex_sum_1533187.txt', 'r')
for line in hand:
    num = re.findall('[0-9]+',line)
    if not num:
        continue
    else:
        for n in num:
            sum += int(n)
print(int(sum))
