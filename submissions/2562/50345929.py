data = []
for i in range(0,9):
    data.append(int(input()))
print(f"{max(data)}\n{data.index(max(data))}")