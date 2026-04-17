a = input("")
people = int(a.split(" ")[0])
cut = int(a.split(" ")[1])

b = input("")
arr = b.split(" ")
arr.sort(reverse=True)


print(arr[cut-1])