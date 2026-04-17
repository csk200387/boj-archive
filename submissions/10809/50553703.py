al = list("abcdefghijklmnopqrstuvwxyz")
b = [-1]*26
a = input()
for i in a :
    b[al.index(i)] = a.index(i)
" ".join(list(map(str,b)))