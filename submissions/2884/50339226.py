num = input("").split(" ")
A = int(num[0])
B = int(num[1])
C = B - 45

if(C < 0):
    A -= 1
    C = 60 + C
print(A,C)