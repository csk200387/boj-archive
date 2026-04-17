import sys
input = lambda:sys.stdin.readline().rstrip()
def change(char, key):
    if not char.isalpha():
        return char
    c = char.lower()
    t = (ord(c) - ord('a') + key) % 26
    t += ord('a')
    result = chr(t)
    return result if char.islower() else result.upper()
while True:
    line = input()
    if line == "#":break
    
    for i in range(26):
        arr = [change(c, i) for c in line]
        if arr[-1] == "A":
            break
    print(*arr[:-1], sep="")