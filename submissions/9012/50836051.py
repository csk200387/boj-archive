def r(str):
	str.replace("()","")
num = int(input())
for i in range(0,num):
	a = input()
	while a.find("()") != -1:
		a = a.replace("()","")
	print("YES" if len(a) == 0 else "NO")