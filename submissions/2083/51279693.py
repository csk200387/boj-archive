import sys
input = lambda:sys.stdin.readline().rstrip()
while True :
    inp = input()
    name, age, weight = inp.split()
    if inp == "# 0 0" :
        break
    elif int(age) > 17 or int(weight) >= 80 :
        print(name, "Senior")
    else :
        print(name, "Junior")