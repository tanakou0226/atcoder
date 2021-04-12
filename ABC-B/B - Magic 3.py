N, S, D = input().split()
N = int(N)
S = int(S)
D = int(D)
xy = [map(int, input().split()) for _ in range(N)]
X, Y = [list(i) for i in zip(*xy)]

for i in range(N):
    if X[i] < S and Y[i] > D:
        print("Yes")
        exit()
print("No")