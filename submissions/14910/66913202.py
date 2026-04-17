import sys


arr = []

tmp = ""
while True:
    read = sys.stdin.read(1)
    if read == "\n":
        arr.append(int(tmp))
        break
    
    if read == " ":
        arr.append(int(tmp))
        tmp = ""
    else:
        tmp += read
    
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print("Bad")
        exit()
print("Good")