a = input().split()
if len(a[0]*int(a[0])) > int(a[1]) :
    print((a[0]*int(a[1]))[:int(a[1])])
else :
    print(a[0]*int(a[0]))