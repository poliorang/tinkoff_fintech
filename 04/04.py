def step_a(point):
    return (point[0] + 1, point[1] + 2)

def step_b(point):
    return (point[0] + 2, point[1] + 1)

def bfs(point):
    a = step_a(point)
    b = step_b(point)

    if a in points.keys():
        points[a] += points[point]

    else:
        if a[0] <= n and a[1] <= m:
            points[a] = points[point]
            queue.insert(0, a)

    if b in points.keys():
        points[b] += points[point]

    else:
        if b[0] <= n and b[1] <= m:
            points[b] = points[point]
            queue.insert(0, b)

    if queue:
        bfs(queue.pop())
    else:
        return 0

n, m = map(int, input().split())
n -= 1
m -= 1
start = (0, 0)
points = {start: 1}
queue = []

bfs(start)

if (n, m) in points.keys():
    print(points[(n, m)])
else:
    print(0)
