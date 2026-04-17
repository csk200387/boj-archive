import sys

arr = []
count = []

while True :
    line = sys.stdin.readline().rstrip()
    if line == "***" :
        break
    else :
        if line in arr :
            count[arr.index(line)] += 1
        else :
            arr.append(line)
            count.append(1)     
if count.count(max(count)) > 1 :
    print("Runoff!")
else :
    print(arr[count.index(max(count))])