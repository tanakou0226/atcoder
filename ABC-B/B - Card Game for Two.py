N = int(input())
a = list(map(int, input().split()))

geme = sorted(a, reverse=True)
Alice = 0
Bob = 0
n = int(len(a))

for i in range(n):
    if i%2 == 0:
        Alice += int(geme[i])
    else:
        Bob += int(geme[i])

print (Alice - Bob)