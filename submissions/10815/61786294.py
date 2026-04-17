import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
h = set(map(int,input().split()))
num = int(input())
dh = tuple(map(int,input().split()))
for i in dh :
	if i in h :
		print(1, end=" ")
	else :
		print(0, end=" ")