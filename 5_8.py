n = int(input())
number = 2
dividers = []
count = 0

while number <= n:
    for k in range(1, number):
        if number % k == 0:
            dividers.append(k)
    if sum(dividers) == number:
        count += 1
    number += 1
    dividers.clear()

print(count)
