import re
p = re.compile('(<([^>]+)>)')
arr = re.split(p,input())
i = 0
while i < len(arr) :
    if p.match(arr[i]) :
        arr[i+1] = ""
        i += 1
    else :
        arr[i] = arr[i][::-1]
    i += 1
print("".join(arr))