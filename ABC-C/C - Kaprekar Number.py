N ,K = input().split()


for i in range(int(K)):
    N = str(N)
    g_1 =''.join(sorted(N))
    g_2 =''.join(sorted(N,reverse=True))
    g_2 = int(g_2)
    g_1 = int(g_1)
    N = g_2 - g_1

print(N)