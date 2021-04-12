N = int(input())
A = []
P = []
X = []
for i in range(N):
    C,D,E = input().split()
    C = int(C)
    D = int(D)
    E = int(E)
    A.append(C)
    P.append(D)
    X.append(E)
 
ans = 100000000000000
count = 0
for i in range(N):
    if X[i] - A[i] > 0:
        can = P[i]
        count += 1
        if can < ans:
            ans = can
 
if count >0:
    print(ans)
else:
    print(-1)