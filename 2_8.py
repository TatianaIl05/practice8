max_res = int(input())
friends_count = 0

if max_res != -1:
    friends_count += 1
    new_res = int(input())

    while new_res != -1:
        friends_count += 1
        new_res = int(input())

print(friends_count)

# Доработанная первая программа

max_res = int(input())
friends_count = 0

if max_res != -1:
    friends_count += 1
    new_res = int(input())

    while new_res != -1:
        if new_res > max_res:
            max_res = new_res
        friends_count += 1
        new_res = int(input())

    print(max_res)
print(friends_count)
