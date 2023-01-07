N = int(input())
pivot=2
while True:
    if N==1 or N==2:
        print(N)
        break
    pivot *= 2
    if pivot>=N:
        print((N-(pivot//2))*2)
        break
    
