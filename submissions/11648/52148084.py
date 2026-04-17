a = input()
count = 0
while True :
    if len(str(a)) == 1 :
        print(count)
        break
    else:
        count += 1
        a = str(eval("*".join(list(a))))