s = input()
t = input()

s = sorted(s)
t = sorted(t)[::-1]
N = len(s)
M = len(t)

n = min(N, M)

for m in range(n):
    if s[m] < t[m]:
        print("Yes")
        exit()
    elif s[m] > t[m]:
        print("No")
        exit()

if N < M:
    print("Yes")
else:
    print("No")
