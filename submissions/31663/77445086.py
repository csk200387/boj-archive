n = int(input())
v = [input() for _ in range(n)]
arr = [0] * 45
cnt = [0] * 45
for string in v:
    for j in range(len(string)):
        arr[j] += ord(string[j])
        cnt[j] += 1
result = ""
for i in range(45):
    if cnt[i] == 0:
        break
    result += chr(arr[i] // cnt[i])

print(result)