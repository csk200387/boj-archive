import sys 
inp = sys.stdin.readlines()
for i in inp :
    while True:
        if i.find("BUG") != 0 :
            i = i.replace("BUG","")
        else :
            print(i, end="")
            break