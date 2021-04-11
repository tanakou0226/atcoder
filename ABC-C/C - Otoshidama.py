N, Y = map(int, input().split())

"""
counter = 0
tenst = []
"""
ans_10000 = -1
ans_5000 = -1
ans_1000 = -1


for a in range(N + 1):
    for b in range(N-a + 1):
        c = N - a - b
        total = 10000*a + 5000 * b + 1000* c
        # counter += 1
        # tenst.append(counter)
        if total == Y:
            ans_10000 = a
            ans_5000 = b
            ans_1000 = c
            break

print (ans_10000, ans_5000, ans_1000)
#print (tenst)