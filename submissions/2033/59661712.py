nm = int(input())
t = 10
if nm < 5 :
    exit(print(0))
if nm < 10 and nm >= 5 :
    exit(print(10))
for i in range(len(str(nm))) :
    if nm > t :
        nm = round(nm+10**(-len(str(nm))-1), -i-1)
    t *= 10
print(int(nm))