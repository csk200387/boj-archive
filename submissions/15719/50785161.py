import sys
from collections import Counter
input = sys.stdin.readline

a = input()
arr = input().rstrip().split()
ee = Counter(arr)
print(max(ee, key=ee.get))