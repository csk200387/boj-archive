try:
    f = open("/dev/stdin", "r")
except FileNotFoundError:
    f = open("./input.txt", "r")
with open("/dev/stdout", "a") as output:
    f.readline()
    while line := f.readline():
        a, b = map(int, line.split())
        output.write(str(a+b)+"\n")
f.close()