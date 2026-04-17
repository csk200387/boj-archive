for i in range(int(input())) :
    a,b = map(int,input().split())
    st = ""
    for l in range(a, b+1) :
        st += str(l)
    print(st.count("0"))