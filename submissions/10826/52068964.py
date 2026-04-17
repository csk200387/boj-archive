import sys
sys.setrecursionlimit(10000)
fib = lambda n: 1 if n<=2 else fib(n-1) + fib(n-2)
print(fib(int(input())))