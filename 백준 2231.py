N = int(input())
for i in range(1, N+1):
    a = 0
    for j in str(i):
        a+=int(j)
    sum = i+a
    if sum == N:
        print(i)
        break
    if i==N:
        print(0)