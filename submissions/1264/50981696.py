import re
while True :
  str = input()
  if str == "#" :
    break
  else :
    m = len(re.findall('[aeiouAEIOU]', str))
    print(m)