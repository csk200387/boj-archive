num = int(input())
sum = 1
stack = 1
while True:
    if sum >= num :
        print(stack-1)
        break
    else :
        stack += 1
        sum += stack