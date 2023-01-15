import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 10000000
graph = [[inf for i in range(n)] for j in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    if graph[u-1][v-1] > w:
        graph[u-1][v-1] = w
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
for i in graph:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
