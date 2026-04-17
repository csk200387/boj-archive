n = input()
res = 0
for i in range(len(n)) :
    if i == len(n)-1 :
        res += (int(n) - 10**(len(n)-1) + 1)*len(n)
    else :
        res += 9*(10**i) * (i+1)
print(res)