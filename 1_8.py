max_res = int(input())
if max_res != -1:
    new_res = int(input())

    while new_res != -1:
        if new_res > max_res:
            max_res = new_res
        new_res = int(input())

    print(max_res)
