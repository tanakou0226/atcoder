N, X = input().split()
N = int(N)
X = int(X)
V = []
P = []
for i in range(N):
    v,p = input().split()
    V.append(int(v))
    P.append(int(p))

alc = 0
for i in range(N):
    alc = alc + V[i]*P[i]
    if alc > X*100:
        print(i+1)
        exit()
print(-1)
