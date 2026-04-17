input()

s = input()
r = ""
for x, y in zip(s, s[::-1]) :
    if x == "?" :
        r += y
    elif y == "?" or x == y != "?":
        r += x
    else :
        r += "?"

print(r.replace("?", "a"))