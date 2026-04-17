import re

def camel(v) : # 정상
    camel_case = re.sub(r'_(.)', lambda m: m.group(1).upper(), v)
    pascal_case = camel_case[0].upper() + camel_case[1:]
    print(v)
    print(re.sub(r'([A-Z])', r'_\1', camel_case).lower())
    print(pascal_case)

def snake(v) :
    camel_case = re.sub(r'_(.)', lambda m: m.group(1).upper(), v)
    pascal_case = camel_case[0].upper() + camel_case[1:]
    print(camel_case)
    print(v)
    print(pascal_case)

def pascal(v) :
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', v).lower()
    camel_case = snake_case.replace('_', ' ').title().replace(' ', '')
    print(camel_case[0].lower()+camel_case[1:])
    print(snake_case)
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