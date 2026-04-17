import math
def f(x, A, B):
    return A*x + B*math.sin(x)
A, B, C = map(int, input().split())
left, right = 0, C/A
while abs(right - left) > 1e-9:
    mid = (left + right) / 2
    if f(mid, A, B) > C:
        right = mid
    else:
        left = mid
print("{:.6f}".format(left))