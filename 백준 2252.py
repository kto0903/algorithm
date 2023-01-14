from collections import deque


def tpsort(indegree, edge, N):
    result = []
    q = deque()
    # bfs를 돌려서 진입차수가 0이면 q에 넣고 그 q와 연결된 노드들을 1씩 빼준다.
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for g in edge[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

    for res in result:
        print(res, end=' ')


N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    indegree[v] += 1
tpsort(indegree, edge, N)
