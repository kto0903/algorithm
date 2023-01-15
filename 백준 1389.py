import sys
def floydwarshall(distance, V):
    for k in range(V+1):#거쳐간 노드
        for i in range(V+1): # 시작노드
            for j in range(V+1): #끝노드
                if distance[i][j] > distance[i][k]+distance[k][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]
    for i in range(1,V+1):
        for j in range(1,V+1):
            if distance[i][j] is not sys.maxsize:
                result[i] += distance[i][j]
V, E = map(int, input().split())
distance = [[sys.maxsize for j in range(V+1)] for i in range(V+1)]
result = [0 for i in range(V+1)]
for i in range(V):
    distance[i][i] = 0
for i in range(E):
    u, v = map(int, input().split())
    distance[u][v] = 1
    distance[v][u] = 1
floydwarshall(distance, V)
print(result.index(min(result[1:])))