a = input()
if a.startswith("0x") :
    b = 16
elif a.startswith("0") :
    b = 8
else :
    b = 10
print(int(a, b))