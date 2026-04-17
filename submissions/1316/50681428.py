num = int(input())
stack = 0
for i in range(num) :
    a = list(input())
    ar = []
    for i in a :
        if i in ar :
            if len(ar)-1 != ar.index(i) :
                stack += 1
                break
        else :
            ar.append(i)
print(num-stack)