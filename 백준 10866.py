import sys
input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
    a = input().split()
    if a[0] == "push_front":
        h.insert(0, a[1])
    elif a[0] == "push_back":
        h.append(a[1])
    elif a[0] == "pop_front":
        if len(h) == 0:
            print(-1)
        else:
            print(h.pop(0))
    elif a[0] == "pop_back":
        if len(h) == 0:
            print(-1)
        else:
            print(h.pop())
    elif a[0] == "size":
        print(len(h))
    elif a[0] == "empty":
        if len(h) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(h) == 0:
            print(-1)
        else:
            print(h[0])
    elif a[0] == "back":
        if len(h) == 0:
            print(-1)
        else:
            print(h[-1])
