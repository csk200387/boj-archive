k, _ = map(int, input().split())
string = input()

for i in string:
    if i in '., ':
        print(i, end='')
    else:
        i = ord(i) + k%26
        if chr(i).isalpha():
            print(chr(i), end='')
        else:
            i -= 26
            print(chr(i), end='')