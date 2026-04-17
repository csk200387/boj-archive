c = int(input())
p = int(input())
arr = []
if c >= 5 :
    arr.append(max(p-500, 0))
if c >= 10 :
    arr.append(int(p*0.9))
if c >= 15 :
    arr.append(max(p-2000, 0))
if c >= 20 :
    arr.append(int(p*0.75))
if c < 5 :
    arr.append(0)
print(min(arr))