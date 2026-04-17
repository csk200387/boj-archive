res = []
for i in range(1,int(input())+1) :
    url = input().split("://")
    protocol = url[0]
    try :
        host = url[1].split(":")[0]
    except :
        host = url[1].split("/")[0]
    try :
        port = url[1].split(":")[1].split("/")[0]
    except :
        port = "<default>"
    try :
        path = "/".join(url[1].split("/")[1:])
        if len(path) == 0 :
            path = "<default>"
    except :
        path = "<default>"
    res.append(f"""URL #{i}
Protocol = {protocol}
Host     = {host.replace("/", "")}
Port     = {port}
Path     = {path}""")
print(*res, sep="\n\n")