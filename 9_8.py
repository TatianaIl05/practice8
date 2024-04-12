n = int(input())
prime_numbers = [2]
number = 3
count_divide = 0
print(2)

while number <= n:
    for item in prime_numbers:
        if number % item != 0:
            count_divide += 1
    if count_divide == len(prime_numbers):
        prime_numbers.append(number)
        print(number)
    count_divide = 0
    number += 1
