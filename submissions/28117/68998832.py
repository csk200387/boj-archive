input()
t = input().count("longlong")
if t == 0:
    print(1)
elif t % 2 == 0:
    print(t*2)
else:
    print(t*2 + 1)