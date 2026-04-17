import datetime
time_format = '%H:%M:%S'
s = datetime.datetime.strptime(input(), time_format)
e = datetime.datetime.strptime(input(), time_format)
result = e - s
print(str(result).split('.')[0])