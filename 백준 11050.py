N, K = map(int, input().split())
a, b, c = 1, 1, 1
for i in range(1, N+1):
    a *= i
for i in range(1, K+1):
    b *= i
for i in range(1, N-K+1):
    c *= i
print(int(a/(b*c)))
