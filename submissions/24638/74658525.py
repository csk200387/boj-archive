a,b = input().split()
c,d = input().split()
if a == 'AD':
    if c == 'AD':
        print(abs(int(b)-int(d)))
    else:
        print(int(c)+int(b)-1)
else:
    if c == 'AD':
        print(int(a)+int(d)-1)
    else:
        print(abs(int(a)-int(c)))