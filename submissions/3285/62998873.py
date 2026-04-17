def DECODE(n:int, s:str):
    left = ""
    right = s
    for i in range(65, 91):
        if chr(i) not in s:
            if len(right) < 27-n:
                right += chr(i)
            else:
                left += chr(i)
    return left + right
d = input()
n = int(input())
s = input()
data = DECODE(n, d)
for i in range(len(s)):
    print(chr(data.index(s[i])+65), end="")