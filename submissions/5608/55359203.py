import sys
input = lambda:sys.stdin.readline().rstrip()

def transform_data(n, table, m, data):
    transformation_map = {}
    for i in range(n):
        a, b = table[i].split()
        transformation_map[a] = b

    result = []
    for char in data:
        if char in transformation_map:
            result.append(transformation_map[char])
        else:
            result.append(char)

    return ''.join(result)

n = int(input())
table = [input() for i in range(n)]
m = int(input())
data = [input() for i in range(m)]
print(transform_data(n, table, m, data))