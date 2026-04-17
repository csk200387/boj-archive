s = input()
for i in range(1, s.count("w")+1):
    t = "w"*i+"o"*i+"l"*i+"f"*i
    s = s.replace(t, "")
print(0 if s else 1)