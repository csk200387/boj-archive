from datetime import datetime
now = datetime.strptime(input(), "%H:%M:%S")
past = datetime.strptime(input(), "%H:%M:%S")
diff = past-now
print(diff)