inp = input()
text = inp.split(":")
ar = []
if text[0] == '':
    text = text[1:]
if text[-1] == '':
    text = text[:-1]
for i in text :
    if i == '' :
        for _ in range(9-len(text)) :
            ar.append('0000')
    else :
        a = i.zfill(4)
        ar.append(a)
print(':'.join(ar))