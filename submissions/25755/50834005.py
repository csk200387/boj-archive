import sys
from collections import Counter
input = sys.stdin.readline

arr = []
a = input().rstrip().split()
dir = a[0]
arr_size = int(a[1])

if dir == "U" or dir == "D" :
	for i in range(arr_size) :
		tmp = input().rstrip().replace("2","5").replace("3","?").replace("4","?").replace("5","2").replace("6","?").replace("7","?").replace("9","?").split()
		arr.append(tmp)
else :
	for i in range(arr_size) :
		tmp = input().rstrip().replace("2","5").replace("4","?").replace("5","2").replace("6","?").replace("7","?").replace("9","?").split()
		arr.append(tmp)

if dir == "L" or dir == "R" :
    for i in arr :
        i.reverse()
    arr.reverse()
    for i in arr :
        print(i)
        
if dir == "U" or dir == "D" :
    arr.reverse()
    for i in arr :
        print(" ".join(i))