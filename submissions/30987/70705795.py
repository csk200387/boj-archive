A,B=map(int,input().split())
a,b,c,d,e=map(int,input().split())
s=lambda X:1/3*a*(X**3)+1/2*(b-d)*(X**2)+(c-e)*X
print(int(s(B)-s(A)))