for i in range(int(input())):
    n = input()
    if (int(n)+1) % int(n[-2:]) == 0:
        print("Good")
    else:
        print("Bye")