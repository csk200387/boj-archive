import math
input()
A = eval(input().replace(" ", "*"))
input()
B = eval(input().replace(" ", "*"))
print(str(math.gcd(A, B))[-9:])