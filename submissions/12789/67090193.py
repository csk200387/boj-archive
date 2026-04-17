n = int(input())
arr = list(map(int, input().split()))
t = []
next = 1
for i in arr:
	t += [i]
	while t and t[-1] == next:
		t.pop()
		next += 1
	if len(t) > 1 and t[-1] > t[-2]:
		print("Sad")
		exit()
print("Sad" if t else "Nice")