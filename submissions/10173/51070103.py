import sys
input = lambda:sys.stdin.readline().rstrip()
while True :
    str = input()
    if str == "EOI" :
        break
    elif str.lower().find("nemo") != -1 :
        print("Found")
    else :
        print("Missing")