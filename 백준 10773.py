N = int(input())
result = []
for i in range(N):
    num = int(input())
    if num == 0:
        del result[-1]
    else:
        result.append(num)
print(sum(result))
