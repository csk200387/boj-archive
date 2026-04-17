time, drink = map(int, input().split())
def is_launch(time):
    if 12 <= time and time <= 16:
        return True
    return False

if drink == 1 or not is_launch(time):
    print(280)
else:
    print(320)