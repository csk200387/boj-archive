nm = int(input())
t = 10
for i in range(len(str(nm))) :
    if nm > t :
        nm = round(nm+10**(-len(str(nm))-1), -i-1)
    t *= 10
print(int(nm))