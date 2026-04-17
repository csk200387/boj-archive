import sys
input = lambda:sys.stdin.read().lower()
a = input().split("\n")
for i in a :
    if i == "" :
        break
    elif "problem" in i :
        print("yes")
    else :
        print("no")