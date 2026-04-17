import re
r = re.findall(r'[A-Z]',input())
t = "love" if "".join(r) == "UCPC" else "hate"
print("I",t,"UCPC")