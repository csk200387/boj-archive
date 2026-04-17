n = int(input())
a_1 = 1
r = 4
S_n = a_1 * (1 - r**n) / (1 - r)
print(int(S_n)%500000009)