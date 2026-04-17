arr = input().split()
arr = [arr[0][0].upper()]+[i[0].upper() for i in arr[1::] if i not in ['i','pa','te','ni','niti','a','ali','nego','no','ili']]
print(*arr, sep="")