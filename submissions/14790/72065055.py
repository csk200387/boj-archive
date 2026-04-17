import sys
input = lambda:sys.stdin.readline().rstrip()

for i in range(int(input())):
    data = input()
    
    while True:
        if data == "".join(sorted(data)):
            print(f"Case #{i+1}: {data}")
            break
        else:
            data = str(int(data)-1)