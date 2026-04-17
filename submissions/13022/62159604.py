s = input()
for i in range(s.count("w"), 0, -1):
    t = "w"*i+"o"*i+"l"*i+"f"*i
    s = s.replace(t, "")
print(0 if s else 1)