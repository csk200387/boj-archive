import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();
        int N = sc.nextInt();
        if (N == 1) {
            System.out.println("-1");
        }
        else {
            int res = (int) Math.ceil(N * K / (N - 1));
            if (N * K % (N - 1) != 0) {
                res += 1;
            }
            System.out.println(res);
        }
        sc.close();
    }
}