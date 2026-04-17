num = int(input())
sum = 0
stack = 0
while True:
    if sum >= num :
        if num == 0 :
            print(0)
        else :
            print(stack-1)
            break
    else :
        sum += stack
        stack += 1