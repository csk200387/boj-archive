d=input()
u=d.index('U')
f=d.rindex('F')
print('-'*u+'U'+'C'*(f-u-1)+'F'+'-'*(len(d)-f-1))