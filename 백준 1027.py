a=int(input())
height=list(map(int,input().split()))#높이를 리스트에 저장한다. 
sight=[0  for _ in range(a)]
for i in range(a-1): #for문을 두번 쓰는데 만약 자신이 오른쪽의 건물이 보이면 이 건물도 왼쪽의 내가 보인다
    maxp = float("-inf") 
    minp = float("-inf")
    for j in range(i+1,a): #그러므로 자신기준 왼쪽 건물을 보는것을 무시한다.
        pivot=(height[j]-height[i])/(j-i) #기울기를 구하고
        if pivot>=0.0:
            if pivot>maxp: #만약 기울기가 양수이면 지금까지 기울기의 최댓값 보다 크면 보인다.
                sight[i]+=1
                sight[j]+=1
                maxp=pivot
        if pivot<0.0:
            if pivot>minp: #만약 기울기가 음수면 지금까지 음의기울기의 최댓값보다 크면 보이는데
                if maxp<0: #만약 기울기가 하나라도 0보다 크거나 같으면 음의 기울기를 가지는 건물 사이는 안보인다.
                    sight[i] += 1
                    sight[j] += 1
                    minp = pivot
print(max(sight))