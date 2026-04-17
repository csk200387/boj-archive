with open("/dev/stdin", "r") as f:
    f.readline()

    while line := f.readline():
        a, b = map(int, line.split())
        with open("/dev/stdout", "a") as output:
            output.write(str(a+b)+"\n")