inp = input("")
list1 = inp.split()
if sorted(list1) == list1 :
  print("ascending")
elif sorted(list1, reverse=True) == list1 :
  print("descending")
else :
  print("mixed")