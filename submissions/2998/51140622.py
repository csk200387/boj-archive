i = input()
if len(i)%3 != 0 :
    i = "0"*(3-len(i)%3)+i
print(oct(int(i,2))[2::])