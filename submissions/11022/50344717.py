num = int(input(""))

for i in range(0,num):
    temp = input("").split(" ")
    A = int(temp[0])
    B = int(temp[1])
    print("Case #{0}: {1}".format(i+1, A+B))