d={"Q": "W","W": "E","E": "R","R": "T","T": "Y","Y": "U","U": "I","I": "O","O": "P","A": "S","S": "D","D": "F","F": "G","G": "H","H": "J","J": "K","K": "L","Z": "X","X": "C","C": "V","V": "B","B": "N","N": "M"}
r=""
for t in input():
 if t.islower():r+=t
 else:
  if t in d:r+=d[t]
  else:r+=t.lower()
print(r)