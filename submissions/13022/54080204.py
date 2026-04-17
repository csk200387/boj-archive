import re
data = input()
if re.fullmatch(r"(w+o+l+f+)+", data) != None :
    for i in re.findall(r"w+o+l+f+", data) :
        count = "{"+str(i.count("w"))+"}"
        if re.fullmatch(f"w{count}o{count}l{count}f{count}", i) != None :
            print(1)
        else :
            print(0)
else :
    print(0)