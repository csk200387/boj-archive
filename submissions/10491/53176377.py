import sys
input = lambda:sys.stdin.read()
a = input().split("\n")
for i in a :
    i = i.lower()
    if i.count("problem") > 0 :
        print("yes")
    else :
        print("no")