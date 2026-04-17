import sys

mem = []

while True:
    data = sys.stdin.readline().strip("\n")
    if data.isdigit():
        mem.append(int(data, 2))
    if len(mem) == 32:
        break


adder = 0
pc = 0
while True:
    cmd = mem[pc] // (2**5)
    value = mem[pc] % (2**5)
    pc += 1
    pc %= 32
    match cmd:
        case 0:
            mem[value] = adder

        case 1:
            adder = mem[value]

        case 2:
            if adder == 0b0:
                pc = value

        case 3:
            pass

        case 4:
            adder = (adder + 255) % (2**8)

        case 5:
            adder = (adder + 1) % (2**8)

        case 6:
            pc = value

        case 7:
            break
        
print(f"{adder:08b}")