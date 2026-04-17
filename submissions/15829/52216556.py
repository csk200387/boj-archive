t = input()
s = input()
res = 0
def aln(st) :
    return ord(st)-96
def pro(m, n) :
    if n == 1 :
        return m
    if n % 2 == 0 :
        a = pro(n//2, m)
        return a * a
    else :
        a = pro(n//2, m)
        return a * a * m
for i in range(len(s)) :
    tmp = aln(s[i])
    res += tmp*pro(31,i)
print(res%1234567891)