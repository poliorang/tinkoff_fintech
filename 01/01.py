a, b, n = map(int, input().split())

num = (a - b) / 2

if (num <= 0) or (num % 1 != 0) or (num < n):
    print('NO')
else:
    print('YES')

