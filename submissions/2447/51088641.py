char = """***
* *
***"""
num = int(input())
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