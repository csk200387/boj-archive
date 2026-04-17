input()
s = {*input().split()}
i = 1
while True:
    if str(i) not in s:
        print(i)
        break
    i += 1