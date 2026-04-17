#include <stdio.h>

int main() {
    int h, m;
    scanf("%d %d", &h, &m);

    m -= 45;

    if (m >= 0) { // m이 45 이상일 때
        printf("%d %d", h, m);
    } else {
        m += 60;
        h -= 1; // 여기서 자정이 들어왔을 때를 생각
        
        if (h < 0) { // 시간이 음수이면
            h += 24;
        }

        printf("%d %d", h, m); // 최종 출력
    }

}