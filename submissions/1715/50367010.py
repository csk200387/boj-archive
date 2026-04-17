num = int(input())
arr = []
for i in range(0,num):
    arr.append(int(input()))
for i in range(0,num):
    arr.append(arr[i] + arr[i+1])
print(eval("+".join(map(str,arr))))