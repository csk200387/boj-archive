from sys import stdin

def convert_minutes(n):
    years = n // (365 * 24 * 60)
    n %= 365 * 24 * 60
    days = n // (24 * 60)
    n %= 24 * 60
    hours = n // 60
    minutes = n % 60
    result = ""
    if years > 0:
        result += f"{years} year(s) "
    if days > 0:
        result += f"{days} day(s) "
    if hours > 0:
        result += f"{hours} hour(s) "
    if minutes > 0:
        result += f"{minutes} minute(s)"

    return result

n = int(stdin.readline())

for i in range(n):
    title, time = stdin.readline().split(",")
    print(title, end=" - ")
    time = int(time) # minutes
    print(convert_minutes(time))