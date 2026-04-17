def caesar(n:int, string:str):
    if string.islower():
        tmp = ord(string) + n
        if tmp > 122:
            tmp -= 26
        return chr(tmp)
    elif string.isupper():
        tmp = ord(string) + n
        if tmp > 90:
            tmp -= 26
        return chr(tmp)
    else:
        return string

k, s = map(int, input().split())
string = input()

for i in string:
    print(caesar(k%26, i), end='')