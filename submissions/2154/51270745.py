num = input()
st = ""
for i in range(1,num+1) :
    st = st + str(i)
    f = st.find(str(num))
    if f != -1 :
        print(f+1)
        break