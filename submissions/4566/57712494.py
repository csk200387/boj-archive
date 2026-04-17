import re
while True :
    inp = input()
    if inp.count('"') > 2 :
        print("not a quine")
    elif inp == "END" :
        break
    else :
        reg = re.fullmatch(r'"(.*)" (.*)', inp)
        if reg == None :
            print("not a quine")
        else :
            if reg.group(1) == reg.group(2) :
                print(f"Quine({reg.group(1)})")
            else :
                print("not a quine")