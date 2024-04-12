n = int(input())
number = 2
dividers = []

while number <= n:
    for k in range(1, number):
        if number % k == 0:
            dividers.append(k)
    if sum(dividers) == number:
        print(number)
    number += 1
    dividers.clear()
