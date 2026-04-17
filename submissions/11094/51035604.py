import sys
input = lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())) :
    str = input()
    if str.find("Simon says") != -1 :
        print(str[10::])