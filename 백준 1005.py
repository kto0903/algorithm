import sys
from collections import deque

a = int(sys.stdin.readline())
result=[]
for i in range(a):
    node, line = map(int,sys.stdin.readline().split())
    costlist = [0]+list(map(int,sys.stdin.readline().split()))
    edge=[[]for _ in range(node+1)]
    indegree = [0 for _ in range(node+1)]
    dp=[0 for _ in range(node+1)]
    for _ in range(line):
        u, v = map(int,sys.stdin.readline().split())
        edge[u].append(v)
        indegree[v] += 1
    
    q = deque()
    for i in range(1,node+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i]=costlist[i]
    while q:
        now = q.popleft()
        for g in edge[now]:
            indegree[g] -= 1
            dp[g]=max(dp[now]+costlist[g],dp[g])
            if indegree[g] == 0:
                q.append(g)
    lastnode = int(sys.stdin.readline())
    
    print(dp[lastnode])
#     result.append(dp[lastnode])
# for k in result:
#     print(k)
