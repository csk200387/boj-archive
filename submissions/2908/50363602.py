a = input().split()
print(int(a[0][::-1]) if int(a[0][::-1]) > int(a[1][::-1]) else int(a[1][::-1]))