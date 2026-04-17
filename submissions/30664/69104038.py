import sys
while True:
    line = sys.stdin.readline()
    if line == "0\n":break
    print("TENTE NOVAMENTE" if int(line)%42 else "PREMIADO")