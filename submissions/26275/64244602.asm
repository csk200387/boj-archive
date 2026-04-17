section .data
    lines db "####################", 0
          db "##J1############J1##", 0
          db "#########J1#########", 0
          db "##J1############J1##", 0
          db "#########J1#########", 0
          db "#########J1#########", 0
          db "##J1############J1##", 0
          db "#########J1#########", 0
          db "##J1############J1##", 0
          db "####################", 0

section .text
    global main

main:
    mov ecx, 10         ; 전체 줄 수 (10줄)
    mov esi, lines      ; lines 문자열 배열의 주소를 esi에 저장

print_loop:
    ; 줄 출력
    mov eax, 4          ; sys_write 시스템 콜 번호
    mov ebx, 1          ; 표준 출력 파일 디스크립터 (stdout)
    mov edx, 22         ; 출력할 문자열 길이 (줄 당 22바이트)
    int 0x80            ; 시스템 콜 실행

    ; 줄 바꾸기
    mov eax, 4          ; sys_write 시스템 콜 번호
    mov ebx, 1          ; 표준 출력 파일 디스크립터 (stdout)
    mov ecx, newline    ; 줄 바꿈 문자열 주소를 ecx에 저장
    mov edx, 1          ; 줄 바꿈 문자열 길이
    int 0x80            ; 시스템 콜 실행

    add esi, 22         ; 다음 줄로 이동
    loop print_loop     ; ecx(줄 수)가 0이 될 때까지 반복

    ; 프로그램 종료
    mov eax, 1          ; sys_exit 시스템 콜 번호
    xor ebx, ebx        ; 종료 코드 0
    int 0x80            ; 시스템 콜 실행

section .data
    newline db 10, 0    ; 줄 바꿈 문자열

section .bss
    resb 1              ; 줄 바꿈 문자열(NULL 포함)을 위한 BSS 섹션
