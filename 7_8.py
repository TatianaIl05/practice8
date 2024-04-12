number = input('Введите число: ')
while not number.isdigit():
    number = input('Ошибка. Попробуйте ещё раз. Введите число: ')
print('Введено целое число:', number)


# Для целых чисел (включая отрицательные)

number = input('Введите число: ')
while not number[1::].isdigit() or number[0] != '-':
    number = input('Ошибка. Попробуйте ещё раз. Введите число: ')
print('Введено целое число:', number)
