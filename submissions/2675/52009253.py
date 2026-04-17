num = int(input(""))
for i in range(0,num):
    a = input().split()
    result = []
    for i in range(0,len(a[1])):
        result.append(a[1][i]*int(a[0]))
    print("".join(result))