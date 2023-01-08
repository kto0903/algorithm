import sys
input = sys.stdin.readline
N = int(input())
result = [0]*10001
for _ in range(N):
    result[int(input())] += 1
for i in range(10001):
    if result[i] != 0:
        for _ in range(result[i]):
            print(i)
