n, data = open(0)
arr = data.split()
result = arr[0][0]
for i in range(1, int(n)):
    if len(arr[i-1]) > len(arr[i]):
        result += " "
    else:
        result += arr[i][len(arr[i-1])-1]
print(result)