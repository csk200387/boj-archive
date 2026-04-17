def chessPlate(num):
    width, length = num*2, num
    origin = []
    for i in range(width):
        if i%2 == 1 :
            a = []
            for d in range(length):
                if d%2 == 0 :
                    a.append(" ")
                if d%2 == 1 :
                    a.append("*")
            origin.append("".join(a))
        if i%2 == 0 :
            a = []
            for d in range(length):
                if d%2 == 0 :
                    a.append("*")
                if d%2 == 1:
                    a.append(" ")
            origin.append("".join(a))
    return origin
for i in chessPlate(int(input())):
    print(i)