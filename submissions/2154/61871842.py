nums = ""
N = int(input())
i = 0
while True:
    if nums.count(str(N)) == 1:
        break
    nums += str(i)
    i += 1
print(nums.index(str(N)))