import datetime
f = '%H:%M:%S'
t1 = datetime.datetime.strptime(input(), f)
t2 = datetime.datetime.strptime(input(), f)
n = t1 + datetime.timedelta(days=1)
d = n - t1 if t2 < t1 else t2 - t1
print(d.strftime(f))