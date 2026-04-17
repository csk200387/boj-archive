num = int(input())
arr = []
for i in range(1,num+1) :
    arr.append(str(i))
print("".join(arr).find(str(num))+1)