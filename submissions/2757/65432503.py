import sys
input = lambda:sys.stdin.readline().rstrip()
def convert(num):
    if num == 0:
        return ""
    else:
        return convert((num-1)//26) + chr((num-1)%26 + ord('A'))
while True:
    data = input()
    if data == "R0C0":
        break
    row = int(data.split("R")[1].split("C")[0])
    col = int(data.split("C")[1])
    print(convert(col) + str(row))