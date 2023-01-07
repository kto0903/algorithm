import sys
def isF(a):
    klist = list(a)
    h = list()
    for i in klist:
        if len(h) == 0:
            h.append(i)
        else:
            if i == "1":
                if h[len(h)-1] == "0":
                    del h[len(h)-1]
                else:
                    h.append(i)
            else:
                h.append(i)
    if len(h) == 0:
        return False
    else:
        return True


N, K = map(int, sys.stdin.readline().split())
alist = [format(i, 'b').zfill(N) for i in range(2**N)]
if N % 2 == 0:
    for i in alist:
        if isF(i) == False:
            alist.remove(i)
if len(alist) <= K:
    print(-1)
else:
    result = list(alist[K])
    for i in range(result):
        if result[i] == "0":
            result[i] = "("
        else:
            result[i] = ")"
    for i in result:
        print(i, end='')
