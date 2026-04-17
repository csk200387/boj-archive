inp = input()
i = 0
for s in inp:
    if s == t[i]:
        i += 1
        if i == 4:
            print("I love UCPC")
            exit(0)
print("I hate UCPC")