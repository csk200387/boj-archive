import re
for i in range(int(input())) :
    t = input()
    if re.fullmatch(r"^[A-F]?A+F+C+[A-F]?$", t) != None :
        print("Infected!")
    else :
        print("Good")