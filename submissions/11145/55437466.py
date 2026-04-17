def is_valid_integer(string):
    # Check if string contains only digits
    return string.isdigit()

t = int(input().strip())
for _ in range(t):
    string = input().strip()
    # Remove leading and trailing whitespaces
    string = string.strip()
    if is_valid_integer(string):
        print(string)
    else:
        print("invalid input")
