import sys 
inp = sys.stdin.readlines()
for i in inp :
    while True:
        print(i.replace("BUG",""),end="")
        break