import sys
import time
from functools import reduce

def Factorial(N):
    checkSize = 5000
    endN = N // checkSize
    facResult = 1
    for fi in range(1, endN + 1):
        facResult = facResult * reduce(lambda x, y : x * y, range((fi-1)*checkSize+1,fi * checkSize+1))

    if (endN * checkSize + 1) != (N+1) :
        facResult = facResult * reduce(lambda x, y : x * y, range(endN * checkSize + 1, N+1))
    return facResult
number = 100000
startTime = time.time()
factorialN = Factorial(number)

sys.stdout.write(f"{factorialN}")