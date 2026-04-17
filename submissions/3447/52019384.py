import sys 
inp = sys.stdin.readlines()
for i in inp :
    while True:
        if i.find("BUG") == -1 :
            print(i, end="")
            break
        else :
            i = i.replace("BUG","")