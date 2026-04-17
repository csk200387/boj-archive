def sol(string:str) -> str:
    r = ""
    for i in range(1, len(string)):
        r += str((int(string[i]) + int(string[i-1])) % 10)
    return r
a,b=open(0)
t = ""
for i in range(16):
    if i%2==0:
        t+=a[i//2]
    else:
        t+=b[i//2]
for _ in range(14):
    t = sol(t)
print(t)