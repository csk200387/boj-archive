import re

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def is_morse_palindrome(string):
    # 정규 표현식을 사용하여 문자열에서 숫자와 알파벳만 추출합니다.
    extracted_str = re.sub('[^0-9a-zA-Z]+', '', string).upper()
    morse_str = ""
    # 추출된 문자열을 모스 부호로 변환합니다.
    for c in extracted_str:
        if c in morse_dict:
            morse_str += morse_dict[c]
    # 모스 부호를 뒤집은 결과가 원래 모스 부호와 같은지 확인합니다.
    return morse_str == morse_str[::-1]

input_str = input()
if re.match("^[0-9a-zA-Z]*$", input_str):
    if is_morse_palindrome(input_str):
        print("YES")
    else:
        print("NO")
else:
    print("NO")