a,b = 0, 1
for i in range(2, int(input())) :
    a, b = b, a+b
print(a+b)