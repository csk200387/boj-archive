import re
data = input()
if re.fullmatch(r"(w+o+l+f+)+", data) != None :
    for i in re.findall(r"w+o+l+f+", data) :
        if i.count("w") == i.count("o") == i.count("l") == i.count("f") :
            print(1)
        else :
            print(0)
            break
else :
    print(0)