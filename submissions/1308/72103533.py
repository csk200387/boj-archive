import datetime
today = datetime.date(*map(int, input().split()))
dday = datetime.date(*map(int, input().split()))
c = dday - today
print(f"D-{c.days}" if c.days < 365*1000 else "gg")