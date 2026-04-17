import sys
input = lambda:sys.stdin.readline().rstrip()

def checkPalin(string, n):
    string = str(string).zfill(n)
    if string == string[::-1]:
        return True
    return False

while True:
    s = input()
    if s == "0":
        break
    n = len(s)
    s = int(s)
    i = 0
    while True:
        if checkPalin(s, n):
            print(i)
            break
        s += 1
        i += 1