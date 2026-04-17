data = input()
key = input()
key = key * (int(len(data) / len(key)) + 1)
def plus(c, n):
    r = (ord(c) - 97 - n)
    if r < 0:r += 26
    return chr(r + 97)
for i in range(len(data)):
    if data[i] == ' ':print(" ", end="")
    else:print(plus(data[i], ord(key[i])-96), end="")