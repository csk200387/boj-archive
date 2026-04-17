d=input()
if not d[0]==d[-1]=='"' or len(d)==2 or d=='"':print("CE")
else:print(d[1:-1])