from datetime import *
ar = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d, m = map(int,input().split())
print(ar[date(2009, m, d).weekday()])