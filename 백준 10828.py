import sys
input=sys.stdin.readline

N=int(input())
h=[]
for i in range(N):
    a=input().split()
    if a[0]=="push":
        h.append(a[1])
    elif a[0]=="pop":
        if len(h)==0:
            print(-1)
        else:
            print(h.pop())
    elif a[0]=="size":
        print(len(h))
    elif a[0]=="empty":
        if len(h) == 0:
            print(1)
        else:
            print(0)
    elif a[0]=="top":
        if len(h) == 0:
            print(-1)
        else:
            print(h[-1])


