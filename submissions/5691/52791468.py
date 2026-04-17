import sys
input = lambda:sys.stdin.readline().rstrip()
while 1:
    a,b=map(int,input().split())
    if a == 0 and b == 0 :
        break
    else :
        print(int((a*2)-b))