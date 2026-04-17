num = int(input())
for i in range(1,num+1) :
    a = num*2 - i*2
    print("*"*i+" "*a+"*"*i)
for i in range(num-1,0,-1):
    a = (num-i)*2
    print("*"*i+" "*a+"*"*i)