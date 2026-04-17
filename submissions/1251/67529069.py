data = input()
arr = []
for start in range(1, len(data)-1):
    for end in range(start+1, len(data)):
        arr.append(data[:start][::-1]+data[start:end][::-1]+data[end:][::-1])
arr.sort()
print(arr[0])