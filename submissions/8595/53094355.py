import re
t=input()
print(sum(list(map(int,re.findall(r"\d+", input())))))