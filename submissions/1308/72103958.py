import datetime
c=(D:=datetime.date(*map(int,input().split())))-(T:=datetime.date(*(a:=list(map(int, input().split())))))
t=(m:=datetime.date(a[0]+1000,a[1],a[2]))-T
print(f"D{c.days}"if c.days<t.days else"gg")