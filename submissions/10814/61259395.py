data = {}
for i in range(int(input())) :
    age, name = input().split()
    data[name] = int(age)
t = sorted(data.items(), key = lambda x : x[1])
for i in t :
    print(i[1], i[0])