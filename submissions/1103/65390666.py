news = input()
data = input()+input()
if news == "S":
    if data == ".OP.":print("T")
    elif data == "I..P":print("F")
    elif data == "O..P":print("Lz")
    else:print("?")
elif news == "N":
    if data == "P..I":print("F")
    elif data == "P..O":print("Lz")
    elif data == ".PO.":print("T")
    else:print("?")
elif news == "E":
    if data == ".PO.":print("Lz")
    elif data == ".PI.":print("F")
    elif data == "O..P":print("T")
    else:print("?")
elif news == "W":
    if data == ".IP.":print("F")
    elif data == ".OP.":print("Lz")
    elif data == "P..O":print("T")
    else:print("?")