num = int(input())
arr = []
for i in range(0,num):
    arr.append(int(input()))
for i in range(0,num-2):
    arr.insert(2*i+1,arr[i] + arr[i+1])
print(eval("+".join(map(str,arr))))