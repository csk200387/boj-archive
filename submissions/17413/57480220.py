string = input()
result = ""
tmp = ""
status = False
for i in string :
    if i == "<" :
        status = True
        result += tmp[::-1]
        tmp = ""
        result += "<"
        continue
    if status :
        result += i
        if i == ">" :
            status = False
            continue
    else :
        if i == " " :
            result += tmp[::-1]
            tmp = ""
            result += " "
        else :
            tmp += i
result += tmp[::-1]
print(result)