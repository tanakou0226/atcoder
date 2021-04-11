N = int(input())
d = [int(input()) for i in range(N)]


new_d = sorted(d)
ans = 1
#print (new_d)


for i in range(N-1):
    i += 1
    if new_d[i] > new_d[i-1]:
        ans += 1
print (ans)
