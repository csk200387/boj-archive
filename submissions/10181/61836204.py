*a,_ = open(0)
for num in a:
    num = int(num)
    s = [i for i in range(1, num) if num % i == 0]
    if sum(s) == num:
        print(f'{num} = {" + ".join(map(str, s))}')
    else:
        print(f'{num} is NOT perfect.')