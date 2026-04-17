data = input()

start, end = 0, 1
arr = [data]
while True:
    if start == len(data)//2:
        break
    elif start <= end:
        start += 1
    else:
        end += 1
    arr.append(data[:start][::-1]+data[start:-end][::-1]+data[-end:][::-1])
arr.sort()
print(arr[0])