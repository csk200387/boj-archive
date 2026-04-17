a = input("")
people = int(a.split(" ")[0])
cut = int(a.split(" ")[1])

b = input("")
arr = b.split(" ")
arr1 = arr.sort(reverse=True)

print(arr1[cut-1])
print(cut-1)