import re
while True :
  str = input()
  if str == "#" :
    break
  else :
    m = len(re.findall('[aeiou]', str, flags=2))
    print(m)