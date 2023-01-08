import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
alist = deque()
result = []
for i in range(1, N+1):
    alist.append(i)
while alist:
    for i in range(K-1):
        alist.append(alist.popleft())
    result.append(alist.popleft())
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">")
