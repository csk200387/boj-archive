ar = [0]
for _ in range(int(input())) :
    inp = input().replace("for","&").replace("while","&")
    ar.append(inp.count("&"))
print(max(ar))