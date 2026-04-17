n = input()
t = int(input())
s = 0
for i in range(t+1):
    s += int(n+"0"*i)
print(s)