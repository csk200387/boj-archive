num = int(input())
arr = []
for i in range(0,num):
    arr.append(int(input()))
for i in range(1,num-1):
    # if len(arr) == 2:
    #     break
    arr[0] = arr[0] + arr[1]
    arr[1] = arr[0]
    #print(arr[0])
print(eval("+".join(map(str,arr))))