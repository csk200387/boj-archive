n = int(input())
ch = input().split()
stack = 0
plus = 0
for i in ch :
    if i == "1" :
        plus += 1
        stack += plus
    else :
        plus = 0

print(stack)