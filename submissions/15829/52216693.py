t = input()
s = input()
res = 0
def aln(st) :
    return ord(st)-96
for i in range(len(s)) :
    tmp = aln(s[i])
    res += tmp*(31**i)
print(res%1234567891)