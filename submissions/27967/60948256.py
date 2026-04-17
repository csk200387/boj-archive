A,s=open(0)
l,t=len(s)//2,s.count
print(s.replace("G","(",l-t("(")).replace("G",")",l-t(")")))