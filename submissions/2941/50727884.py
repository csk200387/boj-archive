a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
str = input()
stack = 0
for i in a :
    if i in str :
        stack += str.count(i)
print(len(str)-stack)