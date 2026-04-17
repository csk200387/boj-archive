import sys
input = sys.stdin.readline

n1 = input()
arr1 = set(input().rstrip().split())
n2 = input()
arr2 = input().rstrip().split()

for i in arr2 :
    if i in arr1 :
        print(1)
    else :
        print(0)