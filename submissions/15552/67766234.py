with open("/dev/stdin", "r") as f:
    with open("/dev/stdout", "a") as output:

        f.readline()

        while line := f.readline():
            a, b = map(int, line.split())
            output.write(str(a+b)+"\n")