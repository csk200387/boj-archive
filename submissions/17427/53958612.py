def measure(num) :
    result = 0
    for i in range(1, int(num**(1/2))+1) :
        if num % i == 0 :
            result += i
            if i != num//i :
                result += num//i
    return result
r = 0
for i in range(1, int(input())+1) :
    r += measure(i)
print(r)