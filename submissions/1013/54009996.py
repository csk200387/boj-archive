import re
for _ in range(int(input())):
    print("NO" if re.fullmatch("(100+1+|01)+",input()) == None else "YES")