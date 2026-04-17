data = input()

for i in range(int(input())) :
    t = input()
    while t in data :
        data = data.replace(t, '')
if len(data) == 0 :
    print('1')
else :
    print('0')