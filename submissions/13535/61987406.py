input()
ip = input()
count = 0
new = ""
while "()" in ip:
  new = ip.replace("()", "", 1)
  if ip != new:
    count += 1
  ip = new
print(count)