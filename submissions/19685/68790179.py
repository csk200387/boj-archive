a, b = map(int, input().split())
def is_palindrome(n):
    num = str(n)
    for i in range(len(num)//2):
        if num[i] != num[-1-i]:
            return False
    return True
def main():
    print_ = print
    for i in range(a, b+1):
        if is_palindrome(i):
            print_("Palindrome!")
        else:
            print_(i)
main()