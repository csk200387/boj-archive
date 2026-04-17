data = input()
arr = [data]
for start in range(1, len(data)//2+1):
    for end in range(1, len(data)//2+1):
        if start+end < len(data):
            arr.append(data[:start][::-1]+data[start:-end][::-1]+data[-end:][::-1])
arr.sort()
print(arr[0])