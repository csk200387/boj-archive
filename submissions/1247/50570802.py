num = int(input())
res = 0
for i in range(num) :
    res += int(input())
print("+" if res > 0 else "-" if res < 0 else "0")