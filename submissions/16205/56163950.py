import re

def camel(v:str) :
    t = v[0].upper()+v[1:]
    arr = re.findall('[A-Z][^A-Z]*', t)
    print(v)
    print("_".join([i.lower() for i in arr]))
    print(t)

def snake(v:str) :
    t = "".join([i.capitalize() for i in v.split("_")])
    print(t[0].lower()+t[1:])
    print(v)
    print(t)
def pascal(v:str) :
    t = re.findall('[A-Z][^A-Z]*', v)
    res = [i.lower() for i in t]
    print(v[0].lower()+v[1:])
    print("_".join(res))
    print(v)

if __name__ == "__main__" :
    n, v = input().split()
    N = int(n)
    if N == 1 :
        camel(v)
    elif N == 2 :
        snake(v)
    elif N == 3 :
        pascal(v)