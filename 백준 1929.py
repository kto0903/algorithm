import sys
input = sys.stdin.readline
a, b = map(int, input().split())
for i in range(a, b+1):
    count = 0
    if i == 1:
        count = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            count = 1
            break
    if count == 0:
        print(i)
