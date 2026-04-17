import re
num = int(input())
reg, exr = input().split("*")
for i in range(num) :
    t = input()
    if re.fullmatch(f"^{reg}.*{exr}$", t) != None :
        print("DA")
    else :
        print("NE")