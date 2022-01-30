n, m = map(int, input().split())

count = 0

while m != 0 and n != 0:
    if n > m:
        n, m = m, n

    while m >= n:
        m -= n
        count += 1

print(count)

