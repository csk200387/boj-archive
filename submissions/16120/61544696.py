a = input()
arr = []
for i in a:
    arr.append(i)
    if arr[-4:] == list("PPAP"):
        for _ in range(4):
            arr.pop()
        arr.append("P")
if arr == list("PPAP") or arr == ["P"]:
    print("PPAP")
else:
    print("NP")