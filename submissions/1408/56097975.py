import datetime
f = '%H:%M:%S'
t1 = datetime.datetime.strptime(input(), f)
t2 = datetime.datetime.strptime(input(), f)
if t2 < t1:
    t2 += datetime.timedelta(days=1)
d = t2 - t1
if d.days == 1:
    d = datetime.timedelta(seconds=0)
print((datetime.datetime.min + d).time().strftime(f))