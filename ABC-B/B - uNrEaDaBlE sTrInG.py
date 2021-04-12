S = input()
S_big = S.upper()
S_small = S.lower()

even = S[::2]
odd = S[1::2]

if S_big[1::2] == odd and S_small[::2] == even:
    print("Yes")
else:
    print("No")