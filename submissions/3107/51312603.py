inp = input()
text = inp.split(":")
ar = []
if text[0] == '':
    text = text[1:]
if text[-1] == '':
    text = text[:-1]
for i in text :
    a = i.zfill(4)
    ar.append(a)
a = ":".join(ar)
if len(text) < 8 :
    tmp = ":".join(['0000']*(8-len(ar)+1))
    print(a.replace("0000",tmp, 1)[:39])
else :
    print(a[:39])