num = int(input(""))
for i in range(0,num):
    temp = input("").split(" ")
    A = int(temp[0])
    B = int(temp[1])
    print(f"Case #{i+1}: {A} + {B} = {A+B}")