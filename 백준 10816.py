from collections import Counter
import sys
input = sys.stdin.readline

_ = input()
N = input().split()
_ = input()
M = input().split()
C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
