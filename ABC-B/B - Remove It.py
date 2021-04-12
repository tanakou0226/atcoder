N, X = input().split()
A = list(map(str, input().split()))
N = int(N)

ans = []
for i in range(N):
    if A[i] != X:
        ans.append(A[i])
    
ans = " ".join(ans)
print (ans)