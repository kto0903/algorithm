import sys
input = sys.stdin.readline
N = int(input())
Plist = list(map(int, input().split()))
M = int(input())
dp = [-sys.maxsize]*(M+1)
for i in range(N-1, -1, -1):
    x = Plist[i]
    for j in range(x, M+1):
        dp[j] = max(dp[j-x]*10+i, i, dp[j])
print(dp[M])
