N = int(input())
A = []
B = []
for i in range(N):
    C,D = input().split()
    C = int(C)
    D = int(D)
    A.append(C)
    B.append(D)

l =[]
s = []
for i in range(N):
    for j in range(N):
        if i == j:
            l.append(A[i] + B[i])
        else:
            s.append(max(A[i],B[j]))
m = min(l)
M = min(s)
ans = min(m,M)
print(ans)