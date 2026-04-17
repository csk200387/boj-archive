inp = input().zfill(2)
temp = inp
result = 0
while True:
    a = int(inp[1])+int(inp[0])
    inp = inp[-1]+str(a)[-1]
    result += 1
    if(inp == temp):
        print(result)
        break