d = input()
while "XXXX" in d:d=d.replace("XXXX", "AAAA")
while "XX" in d:d=d.replace("XX", "BB")
print(-1 if "X" in d else d)