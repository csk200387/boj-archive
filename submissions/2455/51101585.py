import sys
input = lambda:sys.stdin.readline().rstrip()
arr = [int(input().split()[1])]
for i in range(3) :
    b, c = map(int, input().split())
    arr.append(arr[i]+c-b)
print(max(arr))