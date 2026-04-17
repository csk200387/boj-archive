input()
s = input()

l = len(s)//2
open = s.count("(")
close = s.count(")")
for _ in range(l-open):
    s = s.replace("G", "(", 1)
for _ in range(l-close):
    s = s.replace("G", ")", 1)

print(s)