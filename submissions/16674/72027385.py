data = input()
t = set(data)
s = {'2', '0', '1', '8'}

if data.count('2') == data.count('0') == data.count('1') == data.count('8') and s == t:
    print(8)
elif s == t:
    print(2)
elif len(t & s) == len(t):
    print(1)
else:
    print(0)