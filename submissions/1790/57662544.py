import math
n, k = map(int, input().split())
N = math.ceil(n/10)
arr = "".join([str(i)+str(i+1)+str(i+2)+str(i+3)+str(i+4)+str(i+5)+str(i+6)+str(i+7)+str(i+8)+str(i+9) for i in range(0,N*10,10)])
print(arr[k])