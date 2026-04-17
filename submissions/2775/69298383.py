for _ in range(int(input())):
 k = int(input())
 n = int(input())
 arr = [i for i in range(1, n+1)]
 for i in range(k):
  for l in range(1, n):
   arr[l] += arr[l-1]
 print(arr[-1])