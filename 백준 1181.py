import sys
input = sys.stdin.readline
N = int(input())
result = []
for i in range(N):
    result.append(input().strip())
a = set(result)
result = list(a)
result.sort()
result.sort(key=len)
for i in result:
    print(i)
