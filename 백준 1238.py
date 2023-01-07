import sys
import heapq
input = sys.stdin.readline
INF = 1e8
def dijkstra(start):
    q = []
    distance = [INF]*(N+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    return distance
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
result = 0
for i in range(1, N+1):
    a = dijkstra(i)
    b = dijkstra(X)
    result = max(result, a[X]+b[i])
print(result)
