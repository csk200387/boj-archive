import sys
input = lambda:sys.stdin.readline().rstrip()
while 1 :
    inp = input()
    if inp == "#" :
        break
    else :
        str = inp[::-1].split()
        print(*str[::-1], sep=" ")