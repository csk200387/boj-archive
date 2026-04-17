a = input()

while a.count("PPAP") > 0:
    a = a.replace("PPAP", "P", 1)

if a == "P":
    print("PPAP")
else:
    print("NP")