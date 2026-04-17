import re

def camel(v:str) : # 정상
    camel_case = re.sub(r'_(.)', lambda m: m.group(1).upper(), v)
    pascal_case = camel_case[0].upper() + camel_case[1:]
    print(v)
    print(re.sub(r'([A-Z])', r'_\1', camel_case).lower())
    print(v[0].upper()+v[1:])

def snake(v:str) :
    camel_case = re.sub(r'_(.)', lambda m: m.group(1).upper(), v)
    pascal_case = camel_case[0].upper() + camel_case[1:]
    print(camel_case)
    print(v)
    print(pascal_case)

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