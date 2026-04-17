def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

num1, num2 = map(int, input().split())
num2 = int(str(num2)+str(num1))
if isPrime(num1) and isPrime(num2):
    print("Yes")
else:
    print("No")