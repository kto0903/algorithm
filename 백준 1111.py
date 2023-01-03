import sys
input = sys.stdin.readline
a = int(input())
Num = list(map(int, input().split()))
if a == 1:
    print("A")
elif a == 2:
    if Num[1] == Num[0]:
        print(Num[1])
    else:
        print("A")
else:
    if Num[1] == Num[0]:
        A = 0
    else:
        A = (Num[2]-Num[1])//(Num[1]-Num[0])
    B = Num[1]-A*Num[0]
    for i in range(a-1):
        if Num[i]*A+B != Num[i+1]:
            print("B")
            exit()
    print(Num[a-1]*A+B)
