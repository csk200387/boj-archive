char = """***
* *
***"""
num = int(input())
def tlqkf(num) :
    if num == 3 :
        return 1
    elif num == 9 :
        return 2
    elif num == 27 :
        return 3
    elif num == 81 :
        return 4
    elif num == 243 :
        return 5
    elif num == 729 :
        return 6
    elif num == 2187 :
        return 7
    else :
        return 8
num = tlqkf(num)
if num == 1 :
    print(char)
else :
    for _ in range(1,num) :
        arr = []
        for i in range(3) :
            ar = char.split("\n")
            if i == 1 :
                for l in ar :
                    arr.append(l+" "*len(l)+l)
            else :
                for l in ar :
                    arr.append(l*3)
        char = "\n".join(arr)
    print(char)
