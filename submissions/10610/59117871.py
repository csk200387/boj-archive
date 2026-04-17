n = input()
if "0" not in n :
  print(-1)
else :
  n = sorted(map(int, n), reverse=1)
  if sum(n) % 3 != 0 :
    print(-1)
  print(*n, sep="")