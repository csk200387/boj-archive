import sys
input = lambda:sys.stdin.readline().rstrip()
while True :
    str = input()
    if str == "EOI" :
        break
    elif str.find("nemo") != -1 or str.find("Nemo") != -1 :
        print("Found")
    else :
        print("Missing")