income = float(input())
people_count = 0
income_sum = 0

while income != 0:
    income_sum += income
    people_count += 1
    income = float(input())

try:
    print(income_sum/people_count)
except ZeroDivisionError:
    print(0)
