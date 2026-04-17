import sys
input = sys.stdin.readline

arr = []
a = input().rstrip().split()
dir = a[0]
arr_size = int(a[1])
dic = {"1":"1", "2":"5", "5":"2", "8":"8"}
for i in range(arr_size) :
    tmp = input().rstrip().split()
    tmp_arr = []
    for l in tmp :
        try :
            tmp_arr.append(dic[l])
        except :
            tmp_arr.append("?")
    arr.append(tmp_arr)

if dir == "L" or dir == "R" :
    for i in arr :
        i.reverse()
if dir == "U" or dir == "D" :
    arr.reverse()
for i in arr :
    print(" ".join(i))