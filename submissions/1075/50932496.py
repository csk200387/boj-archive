import sys
input = sys.stdin.readline
stack = 0
tmp = int(input().rstrip())
fnum = tmp//100
bnum = tmp%100
div = int(input().rstrip())
res = []
while stack < 100 :
	num = fnum*100 + bnum%100
	if num % div == 0 :
		res.append(bnum%100)
	stack += 1
	bnum += 1
print(str(sorted(res)[0]).zfill(2))