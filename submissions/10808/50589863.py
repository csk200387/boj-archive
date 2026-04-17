al = list("abcdefghijklmnopqrstuvwxyz")
b = [0]*26
a = input()
for i in range(len(a)-1,-1,-1) :
    b[al.index(a[i])] += 1
for i in b :
    print(i)