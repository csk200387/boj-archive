h = []
dh = []
n = int(input())
h = list(map(int,input().split()))
num = int(input())
dh = list(map(int,input().split()))
for i in range(len(dh)) :
	if dh[i] in h :
		dh[i] = 1
	else :
		dh[i] = 0
print(" ".join(map(str,dh)))