import math

A, B = input().split()
A = int(A)
B = int(B)

ans = 0
i = 1
while(i < B):
    i += A-1
    ans += 1
print(ans)