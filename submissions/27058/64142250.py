data, string = open(0)
result = ""
for i in string:
    if i == " ":
        result += " "
    elif i.isalpha():
        if i.isupper():
            result += data[ord(i) - 65].upper()
        else:
            result += data[ord(i) - 97]
print(result)