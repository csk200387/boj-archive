import sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(int(input())) :
  tmp = sorted(list(map(int,input().split()[1::])))
  mx = max(tmp)
  mn = min(tmp)
  gap = []
  for l in range(1,len(tmp)) :
    gap.append(tmp[l] - tmp[l-1])
  print("Class",i+1)
  print(f"Max {mx}, Min {mn}, Largest gap {max(gap)}")