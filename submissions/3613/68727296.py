def is_java(char):
    return char != char.lower()
def is_cpp(char):
    return "_" in char
def se__(char):
    if char[0] == "_" or char[-1] == "_":
        return True
    return False
def main():
    data = input()
    result = ""
    if se__(data) or data[0].isupper() and uandu(data):
        exit(print("Error!"))
    if not is_cpp(data) and data == data.lower():
        print(data)
    elif is_java(data):
        for i in data:
            if i == "_":
                exit(print("Error!"))
            if i.isupper():
                result += "_"+i.lower()
            else:
                result += i
    else:
        idx = 0
        while idx < len(data):
            if data[idx] == "_":
                if idx < len(data):
                    idx += 1
                    if data[idx] == "_":
                        exit(print("Error!"))
                    result += data[idx].upper()
            else:
                result += data[idx]
            idx += 1
    print(result)
main()