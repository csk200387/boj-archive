nm = int(input())
for i in range(len(str(nm))) :
    nm = round(nm+10**(-len(str(nm))-1), -i)
print(int(nm))