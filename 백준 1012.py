from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

a = int(input())


def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return


for i in range(a):
    result = 0
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                result += 1
    print(result)
