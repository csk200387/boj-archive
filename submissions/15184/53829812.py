import re
letter = re.findall("[A-Z]", input().upper())
for i in range(26) :
    char = chr(65+i)
    star = "*"*letter.count(char)
    print(f"{char} | {star}")