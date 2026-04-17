import sys, re, math
input = lambda:sys.stdin.readline().rstrip()
STR = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

st = input()

if st[-1] != "=":
    exit(print("Madness!"))

st = st[:-1]

for i in range(10):
    st = st.replace(STR[i],str(i))

nums = list(map(int, re.split(r"[x\+\-\/]",st)))
op = re.findall(r"[x\+\-\/]",st)

if len(nums)-1 != len(op):
    exit(print("Madness!"))

try:
    value = nums[0]
    for i in range(len(op)):
        if op[i] == "+":
            value += nums[i+1]
        elif op[i] == "-":
            value -= nums[i+1]
        elif op[i] == "x":
            value *= nums[i+1]
        elif op[i] == "/":
            value /= nums[i+1]
            if value < 0:
                value = math.ceil(value)
            else:
                value = math.floor(value)
    print(st+"=")
    res = str(value)
    for i in range(10):
        res = res.replace(str(i),STR[i])
    # print(value)
    print(res)
except:
    exit(print("Madness!"))