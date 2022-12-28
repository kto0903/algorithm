import sys
from collections import deque

a = int(sys.stdin.readline())
result=[]
for i in range(a):
    node, line = map(int,sys.stdin.readline().split()) #건물의 개수, 건설순서 규칙의 총 개수
    costlist = [0]+list(map(int,sys.stdin.readline().split())) #건물당 걸리는 시간
    edge=[[]for _ in range(node+1)] #건물의 연결관리
    indegree = [0 for _ in range(node+1)] #위상 정렬의 연결된곳 관리
    dp=[0 for _ in range(node+1)] 
    for _ in range(line):
        u, v = map(int,sys.stdin.readline().split())
        edge[u].append(v)
        indegree[v] += 1
    
    q = deque()
    for i in range(1,node+1):
        if indegree[i] == 0: #만약 해당하는 연결된 곳이 1이면 deque에 넣는다.
            q.append(i)
            dp[i]=costlist[i]
    while q:
        now = q.popleft()
        for g in edge[now]:
            indegree[g] -= 1 #그리고 연결된 곳이 있으면 그 곳의 indegree를 -1해준다.
            dp[g]=max(dp[now]+costlist[g],dp[g])
            if indegree[g] == 0:
                q.append(g)
    lastnode = int(sys.stdin.readline())
    
    print(dp[lastnode])
