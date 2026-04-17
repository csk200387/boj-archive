d = list(input())
# 게시글에 있는 반례 하나가 맞지않는다
if len(d) <= 3:
    print(0)
else:
    while d[0] == d[-1]:
        d.insert(0, d.pop())

    c = d.count('b')
    cnt = 0
    while d[:c] != ['b']*c:
        t = "".join(d)
        print(t)
        r, l = t.rfind('b'), t.find('r')
        d[r], d[l] = d[l], d[r]
        cnt += 1
    print(cnt)