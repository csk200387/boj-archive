inp = input().split()
a = inp[0]
zero = a[::-1].find('.')
b = int(inp[1])
a_float = float(a)
a_int = int(a_float*(10**zero))
if a_float > 1 :
    result = list(str(a_int**b))
    result.insert(len(result)-(zero*b),".")
    print("".join(result))
else :
    print('0.'+str(a_int**b).zfill(b))