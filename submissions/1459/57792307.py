x, y, w, s = map(int, input().split())
case1 = (x+y) * w
if (x+y) % 2 == 0 :
    # 대각선 갯수가 딱 맞아 떨어지는 경우
    case2 = max(x,y)*s
else :
    case2 = (max(x,y)-1)*s + w
case3 = min(x,y)*s + abs(x-y)*w
print(min(case1, case2, case3))