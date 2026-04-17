import re
res = []
for i in range(1, int(input())+1):
    s = input()
    p = re.match('(http|ftp|gopher)://([\\w.-]+)(?::([\\d]+))?(?:/([\\S]+))?',s)
    res.append(f"""URL #{i}
Protocol = {p.group(1)}
Host     = {p.group(2)}
Port     = {str(p.group(3)).replace("None", "<default>")}
Path     = {str(p.group(4)).replace("None", "<default>")}""")
print(*res, sep="\n\n")