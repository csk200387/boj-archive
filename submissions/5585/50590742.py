num = 1000 - int(input())
a = num//500
b = (num%500)//100
c = ((num%500)%100)//50
d = (((num%500)%100)%50)//10
e = ((((num%500)%100)%50)%10)//5
f = num%5
print(a+b+c+d+e+f)