a=list(map(str.strip, open(0)))
n,d=0,0
for i in range(3):
 if a[i].isdigit():
  n,d=int(a[i]),i
  break
r=n+3-d
if r%3==0 and r%5==0:print("FizzBuzz")
elif r%3==0:print("Fizz")
elif r%5==0:print("Buzz")
else:print(r)