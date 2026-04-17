num = int(input())
for i in range(1,num+1) :
    if i == 1 :
        print(" "*(num-i)+"*")
    else :
        print(" "*(num-i)+"*"+" "*(((i-1)*2)-1)+"*")