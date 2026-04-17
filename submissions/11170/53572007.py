for _ in range(int(input())) :
    st = ""
    n, m = map(int, input().split())
    for i in range(n,m+1) :
        st = st + str(i)
    print(st.count("0"))