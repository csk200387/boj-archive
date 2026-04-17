s=input()
for i in range(s.count("w"),0,-1):s=s.replace("w"*i+"o"*i+"l"*i+"f"*i,"")
print(0 if s else 1)