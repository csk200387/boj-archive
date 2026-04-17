s=input()
for i in range(13,0,-1):s=s.replace("w"*i+"o"*i+"l"*i+"f"*i,"")
print(0 if s else 1)