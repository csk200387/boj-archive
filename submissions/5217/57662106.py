def sol(n) :
    arr = []
    a, b = 1, n-1
    if n < 3 :
        return []
    else :
        while True :
            arr.append(f"{a} {b}")
            b -= 1
            a += 1
            if a >= b :
                break
        return arr
if __name__ == "__main__" :
    for i in range(int(input())) :
        n = int(input())
        arr = ", ".join(sol(n))
        print(f"Pairs for {n}: {arr}")