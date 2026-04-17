num = list(map(int,input().split()))
arr = list(range(1,num[0]+1))
print("<", end="")
for i in range(num[0]) :
    for l in range(num[1]) :
        if l == num[1]-1 :
            if i == num[0]-1 :
                print(arr.pop(0), end=">\n")
            else :
                print(arr.pop(0), end=", ")
        else :
            arr.append(arr.pop(0))