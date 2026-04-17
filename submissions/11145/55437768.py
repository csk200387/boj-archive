def is_valid_integer(string):
    # Check if string contains only digits
    if string.isdigit():
        # Check for leading zeros
        if len(string) > 1 and string[0] == '0':
            return False
        return True
    return False

t = int(input().strip())
for _ in range(t):
    string = input().strip()
    # Remove leading and trailing whitespaces
    string = string.strip()
    if string and string[0] in ['+', '-']:
        if is_valid_integer(string[1:]):
            print(string)
        else:
            print("invalid input")
    elif is_valid_integer(string):
        print(string)
    else:
        print("invalid input")
