def func(rom):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r = 0
    num = 0
    for char in rom:
        n = d[char]
        r += n
        if n > num:
            r -= 2 * num
        num = n
    return r

for _ in range(int(input())) :
    print(func(input()))