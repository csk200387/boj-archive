a,d,k=map(int,input().split())
def c(d):
 if d >= 100:return a
 r=d*0.01*a+(100-d)*0.01*(a+c(d*(1+k*0.01)))
 return r
print(round(c(d),7))