d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for _ in range(int(input())):
    s=input()
    n = d[s[-1]]
    for i in range(len(s)-2,-1,-1):
        n = n - d[s[i]] if d[s[i]] < d[s[i+1]] else n + d[s[i]]
    print(n)