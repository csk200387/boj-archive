num = int(input())
sum = 0
stack = 0
while True:
    if sum >= num :
        print(stack-1)
        break
    else :
        sum += stack
        stack += 1