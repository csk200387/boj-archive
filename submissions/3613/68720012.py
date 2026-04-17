def is_java(char):
    return char != char.lower()
def is_cpp(char):
    return "_" in char
def main():
    data = input()
    result = ""
    if not is_cpp(data) and data == data.lower():
        print(data)
    elif is_java(data):
        for i in data:
            if i.isupper():
                result += "_"+i.lower()
            else:
                result += i
    else:
        idx = 0
        while idx < len(data):
            if data[idx] == "_":
                idx += 1
                result += data[idx].upper()
            else:
                result += data[idx]
            idx += 1
    print(result)
main()