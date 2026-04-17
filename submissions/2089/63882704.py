n = int(input())
r = ''
if n == 0:
    exit(print(0))
while n:
    if n%-2:
        n = n//-2+1
        r = '1'+r
    else:
        n //= -2
        r = '0'+r
print(r)