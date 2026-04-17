import sys, re
input = lambda:sys.stdin.readline().rstrip()
dic = {}
st = ""
t = int(input())
for i in range(t) :
    a, b = input().split()
    dic[a] = b

num = int(input())
for i in range(num) :
    st += input()

for i in dic.keys() :
    st = st.replace(i, dic[i])
print(re.sub(r"[^a-zA-Z0-9]", "", st))