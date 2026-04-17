num = int(input())
if num%2 == 0 :
    print("I LOVE CBNU")
else :
    print("*"*num)
    num = (num+1)//2
    for i in range(1,num+1) :
        print(" "*(num-i)+"*"+" "*(((i-1)*2)-1)+("*" if i > 1 else ""))