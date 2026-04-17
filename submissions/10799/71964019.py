data = input()
arr = []
cnt = 0

for i in range(len(data)):
    if data[i] == "(":
        arr.append("(")
    else:
        if data[i-1] == "(":
            arr.pop()
            cnt += len(arr)
        else:
            arr.pop()
            cnt += 1
print(cnt)