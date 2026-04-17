inp = input()
i = 0
while 1:
    i += 1
    num = str(i)
    while num and inp:
        if num[0] == inp[0]:
            inp = inp[1:]
        num = num[1:]
    if not inp:
        print(i)
        break