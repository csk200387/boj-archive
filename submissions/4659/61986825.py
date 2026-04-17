import re
import sys
while True:
  ip = sys.stdin.readline().rstrip()
  if ip == 'end':
    break
  case1 = len(re.findall('[aeiou]', ip)) != 0
  case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}', ip)) == 0
  case3 = len(re.findall('([a-df-np-z])\\1', ip)) == 0
  if case1 and case2 and case3:
    print(f'<{ip}> is acceptable.')
  else:
    print(f'<{ip}> is not acceptable.')