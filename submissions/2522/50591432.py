num = int(input())
for i in range(1,num) :
    print(("*"*i).rjust(num))
for i in range(num,0,-1) :
    print(("*"*i).rjust(num))