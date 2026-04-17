data = input()
s = {'2', '0', '1', '8'}
if len(s & set(data)) == 0:print(0)
elif data.count('2') == data.count('0') == data.count('1') == data.count('8'):print(8)
elif s == set(data):print(2)
else:print(1)