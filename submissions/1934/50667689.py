import math
num = int(input(()))
for i in range(num):
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    print(int(a * b / math.gcd(a, b)))