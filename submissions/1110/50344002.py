inp = input("")
if(len(inp)<2):
    inp = '0'+inp
temp = inp
result = 0

while True:
    if(len(inp)<2):
        inp = '0'+inp
    a = int(inp[1])+int(inp[0])

    inp = inp[-1]+str(a)[-1]
    result += 1
    if(inp == temp):
        print(result)
        break