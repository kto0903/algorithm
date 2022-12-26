a = int(input())
result=list()
for i in range(a):
    x, y = map(int, input().split()) # 두 지점의 위치를 받아서
    length = y-x #두 지점의 위치를 빼서 두 지점 사이의 거리를 기억해둔다. 
    k=1 #k는 빼는수 즉 처음과 마지막이 1로 시작해서 1로 시작을 해준다. 
    pivot=0 # 작동 횟수
    while 1: 
        if length-k<=0: #만약 length-k가 0보다 작거나 같으면 작동횟수는 1이고 반복문을 나온다.
            pivot+=1
            break
        elif length-(2*k) <= 0:  # 만약 length-(2*k)가 0보다 작거나 같으면 작동횟수는 2이고 반복문을 나온다.
            pivot+=2
            break
        length=length-(2*k) #그것도 아니면 길이 에서 2*k에 해당하는 값을 빼준다.
        k=k+1 #거리가 가까워야 하므로 1을 더해주고
        pivot+=2 #작동횟수에는 2를 더한다. 
    result.append(pivot)
for i in result:
    print(i)

