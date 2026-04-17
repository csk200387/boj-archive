input()
arr = list(map(int, input().split()))
s_arr = sorted(set(arr))
dic = {s_arr[i]: i for i in range(len(s_arr))}
for i in arr:
    print(dic[i], end=' ')