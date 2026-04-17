import java.util.Scanner;

public class Main {
    static double t, cm, kg, bmi;

    static int getBodyClass() {
        bmi = kg / Math.pow(cm / 100, 2);
        if (cm < 140.1) return 6;
        if (140.1 <= cm && cm < 146) return 5;
        if (146 <= cm && cm < 159) return 4;
        if (159 <= cm && cm < 161) {
            if (16 <= bmi && bmi < 35) return 3;
            return 4;
        }
        if (161 <= cm && cm < 204) {
            if (20 <= bmi && bmi < 25) return 1;
            else if ((18.5 <= bmi && bmi < 20) | (25 <= bmi && bmi < 30)) return 2;
            else if ((16 <= bmi && bmi < 18.5) | (30 <= bmi && bmi < 35)) return 3;
            return 4;
        }
        return 4;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        t = scanner.nextInt();
        while (t-- > 0) {
            cm = scanner.nextDouble();
            kg = scanner.nextDouble();
            System.out.println(getBodyClass());
        }
    }
}