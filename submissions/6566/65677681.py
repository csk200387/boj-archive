import sys
input = lambda:sys.stdin.readline().rstrip()
dict = {}
while True:
    try:
        data = input()
        s_data = "".join(sorted(data))
        if s_data in dict:
            dict[s_data].append(data)
        else:
            dict[s_data] = [data]
    except:
        break
stack = 0
for key in sorted(dict.keys(), key=lambda x:(-len(dict[x]), dict[x])):
    print(f"Group of size {len(dict[key])}: {' '.join(sorted(dict[key]))} .")
    stack += 1
    if stack == 5:
        break