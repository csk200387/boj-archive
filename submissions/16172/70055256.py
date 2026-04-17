import re
S = input()
K = input()
s = re.sub('\d', '', S)
if K in s:
    print(1)
else:
    print(0)