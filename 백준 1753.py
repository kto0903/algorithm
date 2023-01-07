import sys
import heapq
input = sys.stdin.readline
INF = 1e8
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #힙에 처음 시작 지점을 넣어준다.
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) #거리와 현재 위치를 가져온다.
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]: #만약 현재 거리보다 작으면
                distance[i[0]] = dist+i[1] #거리를 바꾸어준다. 
                heapq.heappush(q, (dist+i[1], i[0])) #그리고 다익스트라를 이어간다.
V,E=map(int, input().split())
start=int(input())
distance=[INF]*(V+1) #거리를 나타내는 리스트
graph = [[] for _ in range(V+1)] #목적지와 걸리는 시간을 나타내는 리스트
for i in range(E):
    a,b,cost=map(int, input().split())
    graph[a].append((b,cost))
dijkstra(start)
for i in range(1,V+1):
    result=distance[i]
    if distance[i]==100000000.0:
        result="INF"
    print(result)