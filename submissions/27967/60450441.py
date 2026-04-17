input()
s=input()
l=len(s)//2
s=s.replace("G","(",l-s.count("(")).replace("G",")",l-s.count(")"))
print(s)