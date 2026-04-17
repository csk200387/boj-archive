stack = 0
for i in range(5) :
    a = int(input())
    if a <= 40 :
        stack += 40
    else :
        stack += a
print(int(stack/5))