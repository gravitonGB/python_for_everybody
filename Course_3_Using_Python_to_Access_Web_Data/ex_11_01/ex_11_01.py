import re
handle = open('regex_sum_78797.txt')
total = 0
for line in handle:
    line = line.strip()
    num = re.findall('[0-9]+', line)
    results = [int(i) for i in num]
    for j in results:
        total += j
print(total)
