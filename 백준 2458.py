from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
graph = [[0 for i in range(N)] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
result = 0
for i in range(N):
    mine = 0
    for j in range(N):
        mine += graph[i][j]+graph[j][i]
    if mine == N-1:
        result += 1
print(result)
