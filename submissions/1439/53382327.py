a = input()
t1 = len((" ".join(a.split("1"))).split())
t2 = len((" ".join(a.split("0"))).split())
print(t1 if t1 < t2 else t2)