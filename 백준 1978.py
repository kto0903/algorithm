import sys
input = sys.stdin.readline

N = int(input())
alist = list(map(int, input().split()))
result = 0
for i in alist:
    pivot = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            pivot += 1
    if pivot == 0:
        result += 1
print(result)
