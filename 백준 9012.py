import sys
input=sys.stdin.readline

def isVPS(a):
    h=[]
    h.append(0)
    for i in a:
        if i==")" :
            if h[len(h)-1]=="(":
                del h[len(h)-1]
            else:
                h.append(i)
        else:
            h.append(i)
    if len(h)==1:
        print("YES")
    else :
        print("NO")


N=int(input())

for i in range(N):
    a=list(input().strip())
    isVPS(a)
