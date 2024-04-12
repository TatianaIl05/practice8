n = int(input())
spaces = n - 1
stars = 1
while stars <= n:
    print(' '*spaces + '*'*stars)
    spaces -= 1
    stars += 1
