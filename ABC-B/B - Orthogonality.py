N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans = ans + x[i]*y[i]

if ans == 0:
    print("Yes")
else:
    print("No")
