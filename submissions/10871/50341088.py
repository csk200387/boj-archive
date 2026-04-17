num = int(input("").split(" ")[1])
arr = input("").split(" ")
result = []
for i in range(0,len(arr)):
    a = arr[i]
    if int(a) < num:
        result.append(a)
print(" ".join(result))