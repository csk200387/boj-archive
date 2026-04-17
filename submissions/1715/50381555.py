num = int(input())
arr = []
for i in range(0,num):
    arr.append(int(input()))
for i in range(1,num-1):
    arr[0] = arr[0] + arr[1]
    arr[1] = arr[0]
    arr.sort()
print(eval("+".join(map(str,arr))))