num = int(input())
for i in range(1,num+1) :
    if i == num :
        print("*"*(num*2-1))
    else :
        print(" "*(num-i)+"*"+" "*(((i-1)*2)-1)+("*" if i > 1 else ""))