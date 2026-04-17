import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int r, c, q, d, n, p;
        r = scanner.nextInt();
        for (int i = 0; i < r; i++) {
            c = scanner.nextInt();
            q = c / 25;
            d = (c % 25) / 10;
            n = ((c % 25) % 10) / 5;
            p = c % 5;
            System.out.printf("%d %d %d %d\n", q, d, n, p);
        }
        scanner.close();
    }
}