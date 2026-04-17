import re
for _ in range(int(input())) :
    t = input().strip().lstrip("0")
    print(t if re.fullmatch(r"[0-9]*", t) != None else "invalid input")