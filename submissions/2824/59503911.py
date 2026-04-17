import math
a,b,c,d=open(0)
print(str(math.gcd(eval(b.replace(" ","*")), eval(d.replace(" ","*"))))[-9:])