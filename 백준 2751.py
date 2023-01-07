import sys
input=sys.stdin.readline

N=int(input())
result=[]
for i in range(N):
    a=int(input())
    result.append(a)
result.sort()
for i in result:
    print(i)

