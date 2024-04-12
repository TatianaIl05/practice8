str_num = '1'
num = 1
num_sum = 0
while num <= 9:
    num_sum = int(str_num) * 8 + num
    print(f'{str_num} * 8 + {num} = {num_sum}')
    num += 1
    str_num += str(num)
print()
str_num = '1'
num = 2
num_sum = 0
while num <= 10:
    num_sum = int(str_num) * 9 + num
    print(f'{str_num} * 9 + {num} = {num_sum}')
    str_num += str(num)
    num += 1
print()
str_num = '1'
count = 0
num_sum = 0
while count < 9:
    num_sum = int(str_num)**2
    print(f'{str_num} * {str_num} = {num_sum}')
    str_num += '1'
    count += 1
