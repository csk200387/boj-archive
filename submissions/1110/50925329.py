inp = int(input())
temp = inp
result = 0
while True:
    a = inp//10 + inp%10
    inp = ((inp%10)*10)+(a%10)
    result += 1
    if(inp == temp):
        print(result)
        break