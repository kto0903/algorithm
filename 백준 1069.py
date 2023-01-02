import sys
import math
x, y, d, t = map(int, sys.stdin.readline().split())
d = float(d)
t = float(t)
total = math.sqrt(math.pow(x, 2)+math.pow(y, 2))
if total >= d:
    result = min((total//d)*t+(total % d), ((total//d)+1.0)
                 * t+(d-(total % d)), ((total//d)+1.0)*t,total)
elif total < d:
    result=min(t+d-total,2*t,total)
print(result)