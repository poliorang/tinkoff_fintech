def bfs(graph):
    while queue:
        elem = queue.pop()

        for point in graph[elem][0]:
            if point == n:
                return graph[elem][1] + 1

            if point not in visited:
                graph[point][1] = graph[elem][1] + 1
                queue.insert(0, point)

        visited.append(elem)

n = int(input())
up = list(map(int, input().split()))
up = list(reversed(up))
down = list(map(int, input().split()))
down = list(reversed(down))

visited = []
queue = [0]

variat = [[[], 0] for i in range(n)]

for id, elem in enumerate(up):
    for i in range(1, elem + 1):
        x = id + i

        if x <= n:
            if x != n:
                x -= down[x]

            if x >= 0 and x != id:
                variat[id][0].append(x)


ans = bfs(variat)

if ans:
    print(ans)
else:
    print(-1)
