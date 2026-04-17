def factorial(n):
    result = 1
    while n > 1:
        mid = (n + 1) // 2
        left, right = 1, 1
        for i in range(mid):
            left *= i + 1
        for i in range(mid, n + 1):
            right *= i + 1
        result *= left * right
        n = mid - 1
    return result
print(factorial(int(input())))