import sys
input = sys.stdin.readline
while 1:
    a = input().strip()
    alist = list(a)
    blist = alist[::-1]
    if int(a) == 0:
        break
    if alist == blist:
        print("yes")
    else:
        print("no")
