import datetime
today = datetime.date(*(arr:=list(map(int, input().split()))))
dday = datetime.date(*map(int, input().split()))
tmp = datetime.date(arr[0]+1000, arr[1], arr[2])
c = dday - today
t = tmp - today
print(f"D-{c.days}" if c.days < t.days else "gg")