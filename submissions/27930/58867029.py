K, Y = "", ""
k, y = "KOREA", "YONSEI"

inp = input()

ik, iy = 0, 0
for i in inp :
    if i == k[ik] :
        K += i
        ik += 1
    if i == y[iy] :
        Y += i
        iy += 1
    if K == k :
        print(K)
        break
    elif Y == y :
        print(Y)
        break