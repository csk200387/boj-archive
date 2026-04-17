a = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
o1 = input("")
o2 = input("")
o3 = input("")
result = int(str(a[o1]) + str(a[o2]))*(10**a[o3])
print(result)