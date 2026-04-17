a = list(input())
for i in range(0,len(a)):
    if a[i].isupper() == False:
        a[i] = a[i].upper()
    else :
        a[i] = a[i].lower()
print("".join(a))