n=int(input())
s=[]
result=[]
pivot=1
temp=True
for i in range(n):
    num=int(input())
    while pivot<=num:
        s.append(pivot)
        result.append("+")
        pivot+=1
    if s[-1]==num:
        s.pop()
        result.append("-")
    else:
        temp=False
if temp==False:
    print("NO")
else:
    for i in result:
        print(i)