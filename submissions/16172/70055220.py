import re
S = input()
K = input()
s = re.sub('\d', '', S)
print(s, K)
if len(s) < len(K):
    print(0)
elif K in s:
    print(1)
else:
    print(0)