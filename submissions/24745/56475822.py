MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def to_morse_code(s):
    """영문자와 숫자만 추출한 후, 모스 부호로 변환하는 함수"""
    s = ''.join(c.upper() for c in s if c.isalnum())
    return ''.join(MORSE_CODE[c] for c in s)

def is_morse_code_palindrome(s):
    """입력된 문자열이 모스 부호로 대칭인지 확인하는 함수"""
    morse_code = to_morse_code(s)
    return morse_code == morse_code[::-1]

s = "Madam I'm Adam"
print(to_morse_code(s))
if any(c.isalnum() for c in s):
    print("YES" if is_morse_code_palindrome(s) else "NO")
else:
    print("NO")