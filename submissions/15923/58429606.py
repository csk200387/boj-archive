N = int(input())
arr = [[*map(int, input().split())] for i in range(N)]
sum = abs(arr[0][0]-arr[-1][0])
sum += abs(arr[0][1]-arr[-1][1])
for i in range(1, N) :
    sum += abs(arr[i-1][0]-arr[i][0])
    sum += abs(arr[i-1][1]-arr[i][1])
print(sum)