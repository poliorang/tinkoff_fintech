def search(x0, list):
    cur = x0
    for i in range(len(list)):
        if cur > (1e18 + 1):
            return 1
        cur = cur * cur - list[i]
        if cur < 0:
            return 0
    return 1

n = int(input())

numbers = list(map(int, input().split()))
down = 0
up = 1e18

numbers = sorted(numbers)

while up - 1 != down:
    x = (down + up) // 2

    if search(x, numbers):
        up = x
    else:
        down = x

print(int(up))
