# ChatGPT OpenAI
# 수열 A
input()
A = list(map(int,input().split()))

# 수열 A의 길이
n = len(A)

# 가장 긴 증가하는 부분 수열의 길이를 저장할 리스트
lis = [1] * n

# 수열 A를 순회하며, 증가하는 부분 수열을 찾음
for i in range(1, n):
    for j in range(0, i):
        if A[i] > A[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1

# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(lis))