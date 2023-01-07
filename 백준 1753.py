import sys
import heapq
input = sys.stdin.readline
INF = 1e8
def dijkstra(start):
    q = []
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
V,E=map(int, input().split())
start=int(input())
distance=[INF]*(V+1)
graph = [[] for _ in range(V+1)]
for i in range(E):
    a,b,cost=map(int, input().split())
    graph[a].append((b,cost))
dijkstra(start)
for i in range(1,V+1):
    result=distance[i]
    if distance[i]==100000000.0:
        result="INF"
    print(result)