t = input()
arr = [t[i:] for i in range(len(t))]
arr.sort()
print(*arr, sep="\n")