num = int(input())
stack = 0
for i in range(1,num+1):
    if i < 100 :
        stack += 1
    elif i//100 + i%10 == ((i%100)//10)*2 :
        stack += 1
print(stack)