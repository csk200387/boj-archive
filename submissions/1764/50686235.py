import sys
input = sys.stdin.readline
d = set()
b = set()
nums = list(map(int,input().rstrip().split()))
for i in range(nums[0]) :
	d.add(input().rstrip())
for i in range(nums[1]) :
	b.add(input().rstrip())

x = sorted(list(d & b))
print(len(x))
for i in x :
	print(i)