from datetime import datetime
now = datetime.strptime(input(), "%H:%M:%S")
past = datetime.strptime(input(), "%H:%M:%S")
diff = past-now
l = str(diff)
print("0"+l if len(l) == 7 else l)