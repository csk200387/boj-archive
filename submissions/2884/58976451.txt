import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        if (!sc.hasNextInt()) {
            System.exit(0);
        }
        a = sc.nextInt();
        if (!sc.hasNextInt()) {
            System.exit(0);
        }
        b = sc.nextInt();
        c = b - 45;
        if (c < 0) {
            a--;
            if (a < 0)
                a = 23;
            c += 60;
        }
        System.out.println(a + " " + c);
    }
}