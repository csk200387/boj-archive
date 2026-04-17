import sys
from collections import Counter
input = sys.stdin.readline

arr = []
a = input().rstrip().split()
dir = a[0]
arr_size = int(a[1])

for i in range(arr_size) :
	tmp = input().rstrip().split()
	tmp_arr = []
	for l in tmp :
		if l == '1' or l == '8' :
			tmp_arr.append(l)
		elif l == '5' :
			tmp_arr.append('2')
		elif l == '2' :
			tmp_arr.append('5')
		else :
			tmp_arr.append("?")
	arr.append(tmp_arr)

if dir == "L" or dir == "R" :
	for i in arr :
		i.reverse()
	for i in arr :
		print(" ".join(i))

if dir == "U" or dir == "D" :
	arr.reverse()
	for i in arr :
		print(" ".join(i))