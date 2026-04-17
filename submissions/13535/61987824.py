input()
ip = input()

stack = []
count = 0
for i in ip:
  stack += i
  if len(stack) >= 2 and stack[-2] == "(" and stack [-1] == ")":
    stack.pop()
    stack.pop()
    count += 1

print(count)