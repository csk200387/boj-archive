import sys
input = sys.stdin.readline
a = input()
name = input().rstrip()
if name[-1] in ["k", "o", "i", "O", "j", "p", "u", "P", "h", "y", "n", "b", "m", "l"] :
	print(0)
else :
	print(1)