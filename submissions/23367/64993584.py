r = "yuiophjklnm"
word = input()
s = [word[0] in r]
l = "yes"
for i in range(1, len(word)):
    s += [word[i] in r]
    if s[-1] == s[-2]:
        l = "no"
print(l)