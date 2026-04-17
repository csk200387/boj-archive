num = int(input())
for i in range(num):
    if i == 0 :
        print("int a;")
        print("int *ptr = &a;")
    elif i == 1 :
        print("int **ptr2 = &ptr;")
    else :
        print("int "+"*"*(i+1)+"ptr"+str(i+1)+" = &ptr"+str(i)+";")