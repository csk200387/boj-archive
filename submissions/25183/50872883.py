import sys
input = sys.stdin.readline

strlen = int(input().rstrip())
str = input().rstrip()
stack = 0
for i in range(1,strlen) :
    a = ord(str[i-1])-ord(str[i])
    if a == -1 or a == 1 :
        stack += 1
        if stack == 4 :
            print("YES")
            break
    else :
        stack = 0
    if i == strlen-1 :
        print("NO")